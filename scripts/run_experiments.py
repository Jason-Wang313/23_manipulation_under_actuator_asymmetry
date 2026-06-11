from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from asym_manip import run_suite


def main() -> int:
    output_dir = ROOT / "results"
    payload = run_suite(output_dir=output_dir, episodes=160)
    print(f"wrote {payload['episodes']} episode rows to {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
