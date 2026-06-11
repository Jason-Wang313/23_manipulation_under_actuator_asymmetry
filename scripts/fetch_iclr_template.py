from __future__ import annotations

import io
import zipfile
from pathlib import Path
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
TEMPLATE_URL = "https://github.com/ICLR/Master-Template/raw/master/iclr2026.zip"
AUTHOR_GUIDE_URL = "https://iclr.cc/Conferences/2026/AuthorGuide"


FALLBACK_STY = r"""
\NeedsTeXFormat{LaTeX2e}
\ProvidesPackage{iclr2026_conference}[Fallback local ICLR-like style]
\usepackage[letterpaper,margin=1in]{geometry}
\usepackage{times}
\usepackage{natbib}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\lhead{Under review as a conference paper at ICLR 2026}
\cfoot{\thepage}
\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt}
\newcommand{\iclrfinalcopy}{}
""".strip()


FALLBACK_BST = r"""
ENTRY { address author title journal booktitle year volume number pages publisher url doi } {} { label }
FUNCTION {output} { duplicate$ empty$ { pop$ } { write$ } if$ }
FUNCTION {article} { author output " (" output year output "). " output title output ". " output journal output "." output newline$ }
FUNCTION {inproceedings} { author output " (" output year output "). " output title output ". In " output booktitle output "." output newline$ }
FUNCTION {misc} { author output " (" output year output "). " output title output "." output newline$ }
READ
ITERATE {call.type$}
""".strip()


def main() -> int:
    PAPER.mkdir(parents=True, exist_ok=True)
    provenance = [
        "# ICLR Template Provenance",
        "",
        f"- Official author guide checked: {AUTHOR_GUIDE_URL}",
        f"- Template URL used: {TEMPLATE_URL}",
    ]
    try:
        req = Request(TEMPLATE_URL, headers={"User-Agent": "paper23-template-fetcher/1.0"})
        with urlopen(req, timeout=60) as response:
            payload = response.read()
        archive_path = PAPER / "iclr2026.zip"
        archive_path.write_bytes(payload)
        with zipfile.ZipFile(io.BytesIO(payload)) as zf:
            names = zf.namelist()
            extracted = []
            for name in names:
                base = Path(name).name
                if base in {"iclr2026_conference.sty", "iclr2026_conference.bst", "iclr2026_conference.tex"}:
                    (PAPER / base).write_bytes(zf.read(name))
                    extracted.append(base)
        provenance.append(f"- Extracted files: {', '.join(extracted) if extracted else 'none'}")
        if "iclr2026_conference.sty" not in extracted or "iclr2026_conference.bst" not in extracted:
            raise RuntimeError("zip did not contain required sty/bst files")
    except Exception as exc:
        provenance.append(f"- Download failed; wrote fallback style for documented build only: {exc}")
        (PAPER / "iclr2026_conference.sty").write_text(FALLBACK_STY + "\n", encoding="utf-8")
        (PAPER / "iclr2026_conference.bst").write_text(FALLBACK_BST + "\n", encoding="utf-8")
    (PAPER / "template_source.md").write_text("\n".join(provenance) + "\n", encoding="utf-8")
    print("template files prepared in paper/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
