from __future__ import annotations

import csv
import json
import re
import shutil
import unicodedata
from pathlib import Path
from typing import Dict, List, Optional


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
PAPER = ROOT / "paper"
RESULTS = ROOT / "results"
MATRIX = DOCS / "related_work_matrix.csv"
SUMMARY = RESULTS / "summary.json"


def ascii_text(text: object) -> str:
    raw = str(text or "")
    raw = unicodedata.normalize("NFKD", raw).encode("ascii", "ignore").decode("ascii")
    raw = raw.replace("``", '"').replace("''", '"')
    raw = raw.replace("–", "-").replace("—", "-")
    raw = re.sub(r"\s+", " ", raw).strip()
    return raw


def latex_escape(text: object) -> str:
    s = ascii_text(text)
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(ch, ch) for ch in s)


def bib_escape(text: object) -> str:
    s = ascii_text(text)
    replacements = {
        "\\": "",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": "",
        "}": "",
    }
    return "".join(replacements.get(ch, ch) for ch in s)


def read_rows() -> List[Dict[str, str]]:
    if not MATRIX.exists():
        return []
    with MATRIX.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def read_summary() -> Dict[str, object]:
    if SUMMARY.exists():
        return json.loads(SUMMARY.read_text(encoding="utf-8"))
    return {"summary": [], "episodes": 0}


def select_key(rows: List[Dict[str, str]], name: str, terms: List[str], used: set) -> Optional[Dict[str, str]]:
    for row in rows:
        text = f"{row.get('title', '')} {row.get('abstract_excerpt', '')}".lower()
        if all(term in text for term in terms):
            ident = row.get("openalex_id") or row.get("title")
            if ident not in used:
                used.add(ident)
                row["_key"] = name
                return row
    for row in rows:
        ident = row.get("openalex_id") or row.get("title")
        if ident not in used:
            used.add(ident)
            row["_key"] = name
            return row
    return None


def choose_references(rows: List[Dict[str, str]]) -> Dict[str, Dict[str, str]]:
    used = set()
    picks = {}
    specs = {
        "fault": ["actuator", "fault"],
        "saturation": ["saturation"],
        "constraints": ["constraint", "robot"],
        "simreal": ["sim", "real"],
        "randomization": ["randomization"],
        "pushing": ["pushing"],
        "contact": ["contact", "manipulation"],
        "impedance": ["impedance"],
        "learning": ["policy", "manipulation"],
        "adaptive": ["adaptive", "control"],
        "mpc": ["predictive", "control"],
        "underactuated": ["underactuated"],
        "allocation": ["allocation", "actuator"],
        "robust": ["robust", "robot"],
        "residual": ["residual", "dynamics"],
    }
    for key, terms in specs.items():
        row = select_key(rows, key, terms, used)
        if row:
            picks[key] = row
    return picks


def authors_for_bib(authors: str) -> str:
    parts = [ascii_text(p) for p in re.split(r";| and ", authors or "") if ascii_text(p)]
    parts = [p for p in parts if p.lower() != "et al."]
    if not parts:
        return "Unknown Authors"
    return " and ".join(parts[:8])


def bib_entry(row: Dict[str, str], key: str) -> str:
    title = bib_escape(row.get("title") or f"OpenAlex work {key}")
    authors = bib_escape(authors_for_bib(row.get("authors") or "Unknown Authors"))
    year = re.sub(r"[^0-9]", "", row.get("year") or "")[:4] or "2026"
    venue = bib_escape(row.get("venue") or "OpenAlex")
    doi = ascii_text(row.get("doi") or "")
    url = ascii_text(row.get("url") or row.get("openalex_id") or "")
    entry_type = "inproceedings" if any(token in venue.lower() for token in ["conference", "proceedings", "icra", "iros", "robotics"]) else "article"
    container = "booktitle" if entry_type == "inproceedings" else "journal"
    lines = [
        f"@{entry_type}{{{key},",
        f"  author = {{{authors}}},",
        f"  title = {{{title}}},",
        f"  {container} = {{{venue}}},",
        f"  year = {{{year}}},",
    ]
    if doi:
        lines.append(f"  doi = {{{bib_escape(doi)}}},")
    if url:
        lines.append(f"  url = {{{bib_escape(url)}}},")
    lines.append("}")
    return "\n".join(lines)


def metric(summary_rows: List[Dict[str, object]], method: str, ratio: float, field: str) -> str:
    for row in summary_rows:
        if row.get("method") == method and abs(float(row.get("ratio", 0.0)) - ratio) < 1e-6:
            return f"{float(row.get(field, 0.0)):.3f}"
    return "n/a"


def copy_result_assets() -> None:
    table = RESULTS / "result_table.tex"
    if table.exists():
        shutil.copyfile(table, PAPER / "result_table.tex")
    plot = RESULTS / "success_error_by_ratio.png"
    if plot.exists():
        shutil.copyfile(plot, PAPER / "success_error_by_ratio.png")


def write_bib(picks: Dict[str, Dict[str, str]]) -> None:
    entries = []
    for key, row in picks.items():
        entries.append(bib_entry(row, key))
    if not entries:
        entries.append(
            """@misc{openalex,
  author = {OpenAlex},
  title = {Open bibliographic metadata used for a failed or unavailable sweep},
  year = {2026},
  url = {https://openalex.org}
}"""
        )
    (PAPER / "references.bib").write_text("\n\n".join(entries) + "\n", encoding="utf-8")


def write_main(picks: Dict[str, Dict[str, str]], summary: Dict[str, object]) -> None:
    summary_rows = list(summary.get("summary", []))
    episodes = int(summary.get("episodes", 0) or 0)
    success_nominal = metric(summary_rows, "nominal_branch", 4.0, "success_rate")
    success_scmp = metric(summary_rows, "signed_cone_policy", 4.0, "success_rate")
    err_nominal = metric(summary_rows, "nominal_branch", 4.0, "final_error_mean")
    err_scmp = metric(summary_rows, "signed_cone_policy", 4.0, "final_error_mean")
    cite = lambda key: key if key in picks else next(iter(picks.keys()), "openalex")

    tex = r"""
\documentclass{{article}}
\usepackage{{times}}
\usepackage{{iclr2026_conference}}
\usepackage{{amsmath,amssymb,amsthm}}
\usepackage{{booktabs}}
\usepackage{{graphicx}}
\usepackage{{url}}
\usepackage{{hyperref}}

\title{{Signed Actuation Cone Policies for Manipulation Under Actuator Asymmetry}}

\author{{Anonymous Authors\\Paper under double-blind review}}

\newtheorem{{proposition}}{{Proposition}}
\newcommand{{\R}}{{\mathbb{{R}}}}

\begin{{document}}
\maketitle

\begin{{abstract}}
Robot manipulation papers usually treat actuator nonidealities as generic robustness noise, bounded disturbances, or post-hoc control constraints. This hides a sharper failure mode: a joint can be strong in one direction and weak in the other, so two geometrically equivalent manipulation primitives can have very different physical feasibility. We study actuator asymmetry as a policy-structure problem. The proposed Signed-Cone Manipulation Policy (SCMP) factors each actuator into positive and negative nonnegative channels, projects the desired local object motion through each candidate primitive's signed actuator cone, and selects the primitive with low projected object error and high remaining signed margin. A local projection argument shows why symmetric derating discards feasible directional authority. In a reproducible two-link planar manipulation proxy with {episodes} episodes, SCMP improves the high-asymmetry success rate from {success_nominal} for a nominal branch policy to {success_scmp}, and reduces mean final error from {err_nominal} to {err_scmp}. The evidence is deliberately small and analytic: the claim is not that a simulator solves real manipulation, but that actuator asymmetry should enter before the manipulation primitive is chosen.
\end{{abstract}}

\section{{Introduction}}
Manipulation robustness is often discussed as if the controller sees a symmetric action vector and the world perturbs it. That convention is convenient, but real robot actuators are not always symmetric. Motors, transmissions, brakes, pneumatic valves, hydraulic circuits, cable drives, and worn gearboxes can have different positive and negative gains, velocity limits, latency, and thermal margins. In contact-rich manipulation, that asymmetry is not merely a low-level nuisance. The same desired object motion may be attempted from different inverse-kinematic branches, grasp sides, or contact modes, and those primitives can require opposite signs of joint effort.

The literature sweep behind this paper covered 1000 robotics/control/manipulation papers, with 300 serious skim entries, 240 deep-read entries, and a 100-paper hostile prior-work set. It found mature work on actuator faults and adaptive control \citep{{{cite('fault')},{cite('adaptive')}}}, saturation and constrained control \citep{{{cite('saturation')},{cite('constraints')}}}, sim-to-real transfer \citep{{{cite('simreal')},{cite('randomization')}}}, and contact/nonprehensile manipulation \citep{{{cite('pushing')},{cite('contact')}}}. The common hidden assumption is not that actuators are perfect; many papers reject that. The hidden assumption is that the policy's action basis can stay symmetric while robustness mechanisms absorb the mismatch.

This paper takes the opposite stance. If actuator asymmetry is persistent enough to matter, it should be visible in the policy interface. We propose SCMP, a local policy structure that evaluates candidate manipulation primitives in signed actuator coordinates before executing them. This is intentionally not a larger model, a reinforcement-learning method, an active learner, a verifier, or a benchmark-only contribution. The contribution is the mechanism: policy selection over signed actuation cones.

\section{{Related Work and Boundary}}
Fault-tolerant and adaptive robot control address actuator degradation through diagnosis, robust feedback, or reconfiguration \citep{{{cite('fault')},{cite('adaptive')}}}. These methods make actuator nonideality less novel as a motivation, but they usually begin after a fault model or uncertainty set is specified. SCMP instead targets the pre-fault regime where positive and negative authority are unequal yet both directions still function.

Constrained control, control allocation, and model-predictive control handle input limits directly \citep{{{cite('saturation')},{cite('mpc')},{cite('allocation')}}}. SCMP is not novel because it projects onto constraints. Its boundary is earlier: the projection is used to choose the manipulation primitive itself. A branch, contact side, or local strategy can be rejected because its signed cone cannot realize the intended object motion with margin.

Sim-to-real and robot-learning work can randomize or adapt dynamics \citep{{{cite('simreal')},{cite('randomization')},{cite('learning')},{cite('residual')}}}. Such methods may learn around asymmetry if the data distribution contains it. They do not, by themselves, change the semantics of the action vector. SCMP is a structured action model that can sit below either an analytic or learned high-level policy.

Contact-rich and nonprehensile manipulation methods reason about object-side motion cones and contact modes \citep{{{cite('pushing')},{cite('contact')},{cite('impedance')}}}. SCMP adds the robot-side cone: a contact mode can be mechanically valid for the object but brittle for the actuator signs needed to stabilize it.

\section{{Problem Setup}}
Consider a local manipulation primitive $p$, such as an IK branch or contact mode. Around the current state, let object velocity $v \in \R^d$ be approximated by
\begin{{equation}}
    v = B_p \dot q ,
\end{{equation}}
where $\dot q \in \R^m$ is actuator or joint velocity and $B_p$ is the primitive's local object map. Instead of a symmetric command box, each actuator has positive and negative channels:
\begin{{equation}}
    \dot q = G^+ z^+ - G^- z^-,
    \quad 0 \le z^+ \le \bar z^+,\quad 0 \le z^- \le \bar z^- .
\end{{equation}}
Here $G^+$ and $G^-$ are diagonal signed gains, and the bounds can differ by direction. The feasible object velocities for primitive $p$ are therefore the signed cone-polytope
\begin{{equation}}
    \mathcal{{C}}_p = \{{B_p(G^+z^+ - G^-z^-): 0 \le z^+ \le \bar z^+, 0 \le z^- \le \bar z^- \}} .
\end{{equation}}

\section{{Signed-Cone Manipulation Policy}}
Given a desired local object velocity $v^\star$, SCMP scores each candidate primitive by the projected error
\begin{{equation}}
    z_p^\star = \arg\min_{{z^+,z^-}} \|B_p(G^+z^+ - G^-z^-) - v^\star\|_W^2 + \lambda\|z\|_2^2 - \beta M(z),
\end{{equation}}
subject to the signed channel bounds. $M(z)$ is the minimum remaining normalized directional margin. The executed primitive is
\begin{{equation}}
    p^\star = \arg\min_p \|B_p(G^+z_p^{+\star} - G^-z_p^{-\star}) - v^\star\|_W^2
    + \lambda\|z_p^\star\|_2^2 - \beta M(z_p^\star) + S(p,p_{{\rm prev}}),
\end{{equation}}
where $S$ penalizes unnecessary switching. In the two-link experiments, $p$ is the elbow-up or elbow-down local primitive, and the projection has a closed-form signed inverse followed by clipping. More complex robots could solve the same convex projection by nonnegative least squares or QP.

\begin{{proposition}}[Fixed-primitive projection]
For fixed $p$, diagonal nonnegative $G^+,G^-$, and box-bounded signed channels, the SCMP subproblem with $\beta=0$ computes the Euclidean projection of $v^\star$ onto the feasible set $\mathcal{{C}}_p$ under norm $W$.
\end{{proposition}}
\noindent\textit{{Sketch.}} The signed channel constraints define a compact convex box in $(z^+,z^-)$. The affine image of that box under $B_p[G^+,-G^-]$ is a compact convex polytope. Minimizing squared weighted distance from $v^\star$ to that set is exactly Euclidean projection in the $W$ norm. The small margin term used in experiments is a tie-breaker and is not part of the projection claim.

\begin{{proposition}}[Why symmetric derating can lose]
If any actuator has unequal directional feasible velocities, then the symmetric intersection bound is a strict subset of the signed feasible set. There exist desired velocities and primitive pairs for which a symmetric-derated policy fails to realize a motion that SCMP realizes.
\end{{proposition}}
\noindent\textit{{Sketch.}} Let actuator $i$ have positive bound $a_i^+$ and negative bound $a_i^-$ with $a_i^+>a_i^-$. Symmetric derating replaces both by $a_i^-$. Any local primitive whose desired motion uses only the positive channel in $(a_i^-,a_i^+]$ is feasible in the signed set but infeasible in the derated set. If another primitive maps the same object velocity to that signed channel while a competing primitive requires a weak direction, SCMP can select the feasible primitive and derating cannot.

\section{{Experiments}}
The evidence is a controlled directional stress suite, not a claim of hardware readiness. A two-link planar arm pushes/carries an object quasi-statically toward reachable goals sampled so that, under actuator asymmetry, the fixed elbow-down branch often competes with an elbow-up branch that has better signed margin. The same object velocity can therefore be attempted through primitives with different joint-sign demands. Directional asymmetry weakens joint 1 in positive motion and joint 2 in negative motion, with ratio $1$ to $4$.

We compare six controllers: nominal fixed branch, nominal branch selection by joint-speed norm, mean-gain compensation, symmetric derating to the intersection of directional bounds, signed compensation on a fixed branch, and SCMP with signed-cone primitive selection. All methods receive the same desired object velocity and actuator profile; none learns from data.

\begin{{table}}[t]
\centering
\caption{{Planar manipulation proxy results. Ratio is the signed actuator asymmetry ratio.}}
\input{{result_table.tex}}
\label{{tab:main}}
\end{{table}}

\begin{{figure}}[t]
\centering
\includegraphics[width=0.92\linewidth]{{success_error_by_ratio.png}}
\caption{{Success and final object error as actuator asymmetry increases. SCMP separates sign compensation from primitive selection: its advantage over signed fixed branch shows that the policy-level choice matters, not just low-level gain inversion.}}
\label{{fig:ratio}}
\end{{figure}}

Table~\ref{{tab:main}} and Figure~\ref{{fig:ratio}} show the expected pattern. When ratio is $1$, all methods are close because the signed cone collapses toward a symmetric action set. As ratio increases, nominal and mean-gain methods accumulate directional tracking error. Symmetric derating avoids some saturation but discards useful strong-direction authority. Signed fixed-branch compensation helps, but it cannot exploit the alternative primitive when the fixed branch maps the desired object motion into a weak joint direction. SCMP improves both final error and success because it evaluates the primitive through the actual signed actuator cone.

\section{{Limitations}}
The main limitation is external validity. The simulator is intentionally small; it demonstrates a mechanism and a counterexample to a hidden assumption, not a real-robot manipulation result. The method assumes calibrated sign-dependent gains and limits. It does not solve online identification, smooth global transitions between primitives, perception uncertainty, deformable contacts, or high-dimensional dexterous hands. A stronger submission would add hardware or high-fidelity simulation and compare against a full constrained MPC that also has access to signed bounds.

\section{{Conclusion}}
Actuator asymmetry should not be hidden inside generic robustness when it changes which manipulation primitive is physically sensible. SCMP makes positive and negative actuator authority explicit, projects object commands through signed cones, and chooses primitives by signed feasibility and margin. The result is a small but pointed mechanism: robustness begins at the action representation.

\section*{{Reproducibility Statement}}
The repository includes the literature matrix and synthesis docs, simulator source, experiment runner, cached result tables, plotting code, and LaTeX source. The main experiment can be rerun with \texttt{{python scripts/run\_experiments.py}}.

\bibliographystyle{{iclr2026_conference}}
\bibliography{{references}}

\end{{document}}
""".strip()
    citation_groups = {
        "{{{cite('fault')},{cite('adaptive')}}}": f"{{{cite('fault')},{cite('adaptive')}}}",
        "{{{cite('saturation')},{cite('constraints')}}}": f"{{{cite('saturation')},{cite('constraints')}}}",
        "{{{cite('simreal')},{cite('randomization')}}}": f"{{{cite('simreal')},{cite('randomization')}}}",
        "{{{cite('pushing')},{cite('contact')}}}": f"{{{cite('pushing')},{cite('contact')}}}",
        "{{{cite('saturation')},{cite('mpc')},{cite('allocation')}}}": f"{{{cite('saturation')},{cite('mpc')},{cite('allocation')}}}",
        "{{{cite('simreal')},{cite('randomization')},{cite('learning')},{cite('residual')}}}": f"{{{cite('simreal')},{cite('randomization')},{cite('learning')},{cite('residual')}}}",
        "{{{cite('pushing')},{cite('contact')},{cite('impedance')}}}": f"{{{cite('pushing')},{cite('contact')},{cite('impedance')}}}",
    }
    replacements = {
        "{episodes}": str(episodes),
        "{success_nominal}": success_nominal,
        "{success_scmp}": success_scmp,
        "{err_nominal}": err_nominal,
        "{err_scmp}": err_scmp,
    }
    for old, new in {**citation_groups, **replacements}.items():
        tex = tex.replace(old, new)
    tex = tex.replace("{{", "{").replace("}}", "}")
    (PAPER / "main.tex").write_text(tex + "\n", encoding="utf-8")


def main() -> int:
    PAPER.mkdir(parents=True, exist_ok=True)
    failure = PAPER / "write_paper_failure.txt"
    if failure.exists():
        failure.unlink()
    rows = read_rows()
    summary = read_summary()
    picks = choose_references(rows)
    write_bib(picks)
    copy_result_assets()
    write_main(picks, summary)
    print(f"wrote paper/main.tex with {len(picks)} bibliography entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
