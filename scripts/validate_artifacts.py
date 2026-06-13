from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
RESULTS = ROOT / "results"
PAPER = ROOT / "paper"
DOWNLOADS_PDF = Path("C:/Users/wangz/Downloads/23.pdf")


REQUIRED_DOCS = [
    "related_work_matrix.csv",
    "literature_map.md",
    "hostile_prior_work.md",
    "novelty_boundary_map.md",
    "novelty_decision.md",
    "claims.md",
    "reviewer_attacks.md",
    "final_audit.md",
]


def matrix_stats() -> dict:
    path = DOCS / "related_work_matrix.csv"
    if not path.exists():
        return {"rows": 0, "serious": 0, "deep": 0, "hostile": 0, "columns": []}
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
    return {
        "rows": len(rows),
        "serious": sum(1 for row in rows if "serious_skim" in (row.get("sweep_stage") or "")),
        "deep": sum(1 for row in rows if "deep_read" in (row.get("sweep_stage") or "")),
        "hostile": sum(1 for row in rows if row.get("hostile_rank")),
        "columns": reader.fieldnames or [],
    }


def experiment_stats() -> dict:
    path = RESULTS / "summary.json"
    if not path.exists():
        return {
            "episodes": 0,
            "rows": 0,
            "ratio4_scmp_success": None,
            "calibration_stress_rows": 0,
            "calibration_ratio1_scmp_success": None,
        }
    payload = json.loads(path.read_text(encoding="utf-8"))
    rows = payload.get("summary", [])
    calibration_rows = payload.get("calibration_stress", [])
    ratio4 = None
    for row in rows:
        if row.get("method") == "signed_cone_policy" and abs(float(row.get("ratio", 0.0)) - 4.0) < 1e-9:
            ratio4 = row.get("success_rate")
    calibration_ratio1 = None
    for row in calibration_rows:
        if row.get("method") == "signed_cone_policy" and abs(float(row.get("estimated_ratio", 0.0)) - 1.0) < 1e-9:
            calibration_ratio1 = row.get("success_rate")
    return {
        "episodes": payload.get("episodes", 0),
        "rows": len(rows),
        "ratio4_scmp_success": ratio4,
        "calibration_stress_rows": len(calibration_rows),
        "calibration_ratio1_scmp_success": calibration_ratio1,
        "calibration_stress_table_exists": (RESULTS / "calibration_stress_table.tex").exists(),
        "calibration_stress_plot_exists": (RESULTS / "calibration_stress.png").exists(),
    }


def main() -> int:
    docs = {}
    for name in REQUIRED_DOCS:
        path = DOCS / name
        docs[name] = {"exists": path.exists(), "bytes": path.stat().st_size if path.exists() else 0}
    report = {
        "matrix": matrix_stats(),
        "experiments": experiment_stats(),
        "docs": docs,
        "paper_main_exists": (PAPER / "main.tex").exists(),
        "paper_pdf_exists": (PAPER / "main.pdf").exists(),
        "downloads_pdf_exists": DOWNLOADS_PDF.exists(),
    }
    out = DOCS / "validation_report.json"
    out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
