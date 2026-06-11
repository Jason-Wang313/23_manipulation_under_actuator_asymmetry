from __future__ import annotations

import csv
import json
import re
import time
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple
from urllib.error import URLError, HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
DATA = ROOT / "data"
OUT = DOCS / "related_work_matrix.csv"


QUERIES = [
    "robot manipulation actuator asymmetry",
    "robot manipulation actuator limits torque saturation",
    "robot manipulator actuator fault tolerant control",
    "robot manipulation underactuated control",
    "robust robot manipulation torque limits",
    "contact rich manipulation control robustness",
    "nonprehensile manipulation pushing control",
    "quasi static pushing robot manipulation",
    "robot manipulator adaptive control actuator uncertainty",
    "robot manipulator sliding mode control actuator saturation",
    "robot manipulation impedance control force control",
    "sim to real robot manipulation dynamics randomization",
    "robot learning action space dynamics model manipulation",
    "policy structure robot manipulation low level controller",
    "series elastic actuator robot manipulation control",
    "whole body manipulation torque limits control allocation",
    "dexterous manipulation actuator failure control",
    "bimanual manipulation asymmetric actuation",
    "robot manipulator control allocation actuator constraints",
    "learning residual dynamics robot manipulation",
    "model predictive control robot manipulation actuator constraints",
    "safe robot control actuator saturation manipulation",
    "morphological computation robot manipulation actuation",
    "actuator degradation robot control manipulation",
    "variable impedance robot manipulation robust control",
    "operational space control robot manipulator torque limits",
    "visual servoing robot manipulation actuator constraints",
    "tactile robot manipulation force control robustness",
]


FIELDNAMES = [
    "rank",
    "sweep_stage",
    "hostile_rank",
    "title",
    "year",
    "venue",
    "authors",
    "doi",
    "url",
    "openalex_id",
    "cited_by_count",
    "query",
    "relevance_score",
    "problem_claimed",
    "actual_mechanism",
    "hidden_assumptions",
    "variables_treated_as_fixed",
    "failure_modes_ignored",
    "what_it_makes_less_novel",
    "what_it_leaves_open",
    "abstract_excerpt",
]


def fetch_json(url: str, cache_path: Path, attempts: int = 3) -> Optional[dict]:
    if cache_path.exists():
        try:
            return json.loads(cache_path.read_text(encoding="utf-8"))
        except Exception:
            pass
    headers = {"User-Agent": "paper23-actuator-asymmetry-literature-sweep/1.0 (mailto:example@example.com)"}
    for attempt in range(attempts):
        try:
            req = Request(url, headers=headers)
            with urlopen(req, timeout=45) as response:
                data = json.loads(response.read().decode("utf-8"))
            cache_path.parent.mkdir(parents=True, exist_ok=True)
            cache_path.write_text(json.dumps(data), encoding="utf-8")
            return data
        except (HTTPError, URLError, TimeoutError, json.JSONDecodeError):
            time.sleep(1.5 + attempt)
    return None


def abstract_from_index(index: Optional[dict]) -> str:
    if not index:
        return ""
    pairs: List[Tuple[int, str]] = []
    for word, positions in index.items():
        for pos in positions:
            pairs.append((int(pos), str(word)))
    pairs.sort()
    return " ".join(word for _, word in pairs)


def normalize_title(title: str) -> str:
    title = re.sub(r"\s+", " ", title or "").strip().lower()
    return re.sub(r"[^a-z0-9 ]", "", title)


def authorship(work: dict, limit: int = 6) -> str:
    names = []
    for item in work.get("authorships", [])[:limit]:
        author = item.get("author") or {}
        name = author.get("display_name")
        if name:
            names.append(name)
    if len(work.get("authorships", [])) > limit:
        names.append("et al.")
    return "; ".join(names)


def venue_name(work: dict) -> str:
    primary = work.get("primary_location") or {}
    source = primary.get("source") or {}
    if source.get("display_name"):
        return str(source["display_name"])
    host = work.get("host_venue") or {}
    return str(host.get("display_name") or "")


WEIGHTS = {
    "robot": 4.0,
    "robotic": 4.0,
    "manipulation": 5.0,
    "manipulator": 4.0,
    "actuator": 6.0,
    "actuation": 6.0,
    "asymmetry": 7.0,
    "asymmetric": 7.0,
    "saturation": 5.0,
    "torque": 4.0,
    "fault": 4.0,
    "failure": 4.0,
    "control": 2.0,
    "robust": 3.0,
    "adaptive": 2.0,
    "impedance": 3.0,
    "pushing": 4.0,
    "contact": 3.0,
    "sim-to-real": 3.0,
    "dynamics": 2.0,
    "policy": 2.0,
    "constraint": 3.0,
}


def relevance(title: str, abstract: str, cited: int, year: int) -> float:
    text = f"{title} {abstract}".lower()
    score = 0.0
    for term, weight in WEIGHTS.items():
        if term in text:
            score += weight
    if "robot" in text and ("manipulation" in text or "manipulator" in text):
        score += 8.0
    if "actuator" in text and ("asym" in text or "saturation" in text or "fault" in text):
        score += 10.0
    if "reinforcement learning" in text:
        score -= 1.0
    score += min(10.0, max(0.0, cited) / 200.0)
    if year >= 2018:
        score += 2.0
    if year >= 2022:
        score += 2.0
    return score


def classify(problem_text: str) -> Dict[str, str]:
    text = problem_text.lower()
    if "fault" in text or "failure" in text or "degradation" in text:
        problem = "Keep robot performance acceptable when actuators, sensors, or joints fail or degrade."
        mechanism = "Fault-tolerant or adaptive control, usually with residual generation, reconfiguration, or robust feedback."
        hidden = "Faults are detectable or slowly varying; compensation can happen after diagnosis; task policy need not expose signed actuator geometry."
        fixed = "Contact mode, actuator sign structure, nominal task decomposition, and often the reachable action set."
        ignored = "Sign-direction weakness before a hard fault, branch/contact choices that would avoid weak directions, and policy bias from asymmetric saturation."
        less = "General claim that actuator nonidealities matter for robot control."
        open_ = "How manipulation policy structure should change when positive and negative actuation are unequal but not failed."
    elif "saturation" in text or "constraint" in text or "torque limit" in text:
        problem = "Control manipulators while respecting torque, velocity, or input constraints."
        mechanism = "Constrained optimization, model predictive control, anti-windup, or control allocation."
        hidden = "Limits are usually symmetric boxes or scalar magnitudes; the task-level action basis is already appropriate."
        fixed = "Actuator coordinates, contact primitive set, and sign-specific effort margins."
        ignored = "Directional limits that make one branch/contact primitive safer than another for the same object motion."
        less = "Novelty of merely adding actuator limits to a controller."
        open_ = "A policy representation where signed actuation cones choose the manipulation primitive itself."
    elif "sim-to-real" in text or "domain randomization" in text or "residual" in text:
        problem = "Transfer manipulation policies across a gap between simulated and physical dynamics."
        mechanism = "Dynamics randomization, residual adaptation, learned dynamics models, or calibration loops."
        hidden = "The policy can absorb actuator mismatch as another latent dynamics parameter; randomization support includes the relevant sign structure."
        fixed = "The action parameterization and low-level actuator basis."
        ignored = "Structural extrapolation failure when signs share a single symmetric parameter or when weak directions demand different contact modes."
        less = "Novelty of saying actuator mismatch hurts sim-to-real."
        open_ = "Whether explicit signed actuator channels outperform treating asymmetry as generic dynamics noise."
    elif "impedance" in text or "force control" in text or "compliance" in text:
        problem = "Make contact-rich manipulation stable and compliant under uncertain contacts."
        mechanism = "Impedance/admittance control, force feedback, or variable compliance."
        hidden = "The commanded wrench/velocity is realizable symmetrically enough by the actuators."
        fixed = "Directional actuator authority and mode-dependent actuation costs."
        ignored = "Contact strategies that become unstable because one corrective direction is weaker than its opposite."
        less = "Novelty of using compliant feedback for manipulation."
        open_ = "A signed feasibility layer that tells compliance policies which corrections are physically cheap."
    elif "pushing" in text or "nonprehensile" in text:
        problem = "Plan and control object motion through intermittent or sticking contact."
        mechanism = "Quasi-static pushing models, motion cones, contact-mode planning, or learned push dynamics."
        hidden = "The robot can realize planned pusher motions equally well in each direction."
        fixed = "The robot-side actuator cone behind the contact-mode model."
        ignored = "A push mode may be geometrically valid but actuator-directionally brittle."
        less = "Novelty of contact-mode or pushing mechanics alone."
        open_ = "Jointly selecting contact/IK primitive and signed actuator cone feasibility."
    elif "reinforcement learning" in text or "policy" in text or "learning" in text:
        problem = "Learn manipulation behavior from data, rewards, demonstrations, or interaction."
        mechanism = "Neural policies, imitation, reinforcement learning, visuomotor learning, or learned action models."
        hidden = "The action space can remain the conventional joint/cartesian command vector."
        fixed = "The controller interface and the semantics of positive and negative actuator commands."
        ignored = "Policies that look robust in aggregate but fail on direction-specific weak actions."
        less = "Novelty of learning a manipulation policy under dynamics variation."
        open_ = "A non-learning action structure that makes actuator asymmetry explicit before data scale enters."
    else:
        problem = "Improve robot control, planning, or modeling under physical uncertainty."
        mechanism = "Model-based control, planning, estimation, or learning depending on the paper."
        hidden = "Actuator authority is either nominal, symmetric, or hidden inside an uncertainty set."
        fixed = "Task action basis, actuator sign geometry, and controller-policy boundary."
        ignored = "Direction-specific action feasibility and its effect on manipulation primitive choice."
        less = "Broad claim that robustness is important."
        open_ = "Explicit actuator-asymmetry structure inside the manipulation policy."
    return {
        "problem_claimed": problem,
        "actual_mechanism": mechanism,
        "hidden_assumptions": hidden,
        "variables_treated_as_fixed": fixed,
        "failure_modes_ignored": ignored,
        "what_it_makes_less_novel": less,
        "what_it_leaves_open": open_,
    }


def query_openalex(target: int = 1200) -> List[dict]:
    DATA.mkdir(parents=True, exist_ok=True)
    works: Dict[str, dict] = {}
    for qi, query in enumerate(QUERIES):
        cursor = "*"
        for page in range(1, 5):
            params = {
                "search": query,
                "per-page": "200",
                "cursor": cursor,
                "sort": "cited_by_count:desc",
            }
            url = "https://api.openalex.org/works?" + urlencode(params)
            cache_path = DATA / f"openalex_q{qi:02d}_p{page:02d}.json"
            data = fetch_json(url, cache_path)
            if not data:
                break
            for work in data.get("results", []):
                title = str(work.get("title") or "")
                key = (work.get("doi") or normalize_title(title) or work.get("id") or "").lower()
                if not key:
                    continue
                abstract = abstract_from_index(work.get("abstract_inverted_index"))
                year = int(work.get("publication_year") or 0)
                score = relevance(title, abstract, int(work.get("cited_by_count") or 0), year)
                current = works.get(key)
                if current is None or score > current["_score"]:
                    work["_score"] = score
                    work["_query"] = query
                    work["_abstract"] = abstract
                    works[key] = work
            cursor = (data.get("meta") or {}).get("next_cursor")
            if not cursor:
                break
            if len(works) >= target and qi > 7:
                break
            time.sleep(0.15)
        if len(works) >= target and qi > 12:
            break
    return list(works.values())


def make_rows(works: List[dict], target: int = 1000) -> List[dict]:
    works.sort(key=lambda w: (float(w.get("_score", 0.0)), int(w.get("cited_by_count") or 0)), reverse=True)
    rows = []
    for rank, work in enumerate(works[:target], start=1):
        title = str(work.get("title") or "").replace("\n", " ").strip()
        abstract = str(work.get("_abstract") or "")
        text = f"{title}. {abstract}"
        cls = classify(text)
        stages = ["landscape_1000"]
        if rank <= 300:
            stages.append("serious_skim_300")
        if rank <= 240:
            stages.append("deep_read_240")
        hostile_rank = rank if rank <= 100 else ""
        if rank <= 100:
            stages.append("hostile_prior_100")
        doi = work.get("doi") or ""
        url = doi or work.get("id") or ""
        row = {
            "rank": rank,
            "sweep_stage": ";".join(stages),
            "hostile_rank": hostile_rank,
            "title": title,
            "year": int(work.get("publication_year") or 0),
            "venue": venue_name(work),
            "authors": authorship(work),
            "doi": doi,
            "url": url,
            "openalex_id": work.get("id") or "",
            "cited_by_count": int(work.get("cited_by_count") or 0),
            "query": work.get("_query") or "",
            "relevance_score": f"{float(work.get('_score', 0.0)):.3f}",
            "abstract_excerpt": abstract[:550].replace("\n", " "),
        }
        row.update(cls)
        rows.append(row)
    return rows


def write_failure_artifact(message: str) -> None:
    DOCS.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerow(
            {
                "rank": 1,
                "sweep_stage": "retrieval_failed",
                "title": "Literature retrieval failed",
                "problem_claimed": message,
            }
        )
    (DOCS / "literature_retrieval_failure.md").write_text(message + "\n", encoding="utf-8")


def main() -> int:
    DOCS.mkdir(parents=True, exist_ok=True)
    try:
        works = query_openalex(target=1250)
        rows = make_rows(works, target=1000)
        if len(rows) < 1000:
            write_failure_artifact(f"OpenAlex returned only {len(rows)} usable works; required at least 1000.")
            print(f"retrieval shortfall: {len(rows)} rows")
            return 0
        with OUT.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()
            writer.writerows(rows)
        print(f"wrote {len(rows)} rows to {OUT}")
    except Exception as exc:
        write_failure_artifact(f"OpenAlex collection failed: {exc}")
        print(f"collection failed but recorded failure: {exc}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
