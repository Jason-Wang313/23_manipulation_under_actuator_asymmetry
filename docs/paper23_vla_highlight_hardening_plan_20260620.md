# Paper23 VLA Highlight Hardening Plan

Date: 2026-06-20

## Objective

Make `C:/Users/wangz/Downloads/23.pdf` match the visible VLA-v4 role model's
boxed-link behavior while preserving the final 25-page actuator-asymmetry
paper:

- citation links use green one-point boxes;
- internal figure/table/section links use red one-point boxes;
- URL links use green one-point boxes, not cyan boxes;
- the final PDF is rebuilt, copied only to Downloads, visually checked, and
  leaves no local `paper/main.pdf`.

## Plan-Start Evidence

Baseline artifact:

- Canonical PDF: `C:/Users/wangz/Downloads/23.pdf`
- Pages: 25
- Size: 360,190 bytes
- SHA256: `84342525B234DFCBF4F1D23DD11349BDF2D179953A42A0110D60078403247519`
- Local `paper/main.pdf`: absent
- Repository state: clean against `origin/master`

Baseline link inventory from the current Downloads PDF:

- Link pages: `[(2, 31), (5, 1), (6, 1), (8, 1), (12, 9), (13, 13)]`
- Annotation colors: green = 31, red = 3, cyan = 22
- Border widths: `(0, 0, 1)` for all 56 link annotations

Source finding:

- `paper/main.tex` is the active manuscript source.
- The preamble currently loads plain `hyperref` but has no explicit VLA-style
  `\hypersetup`.
- The current PDF already has green citation boxes and red internal boxes, but
  URL links are cyan. The target is to make URL boxes green, matching the VLA
  role model.
- `scripts/build_paper.ps1` copies the final PDF to Downloads; if it leaves
  `paper/main.pdf`, remove that local PDF after verification.

## Role-Model Target

Install the same explicit hyperref policy as the visible VLA-v4 role model:

```tex
\usepackage{hyperref}
\hypersetup{
  colorlinks=false,
  pdfborder={0 0 1},
  citebordercolor={0 1 0},
  linkbordercolor={1 0 0},
  urlbordercolor={0 1 0}
}
```

## Execution Plan

1. Add the VLA `\hypersetup` block immediately after `\usepackage{hyperref}`
   in `paper/main.tex`.
2. Rebuild with `scripts/build_paper.ps1`, including BibTeX, so the final PDF
   is copied to Downloads.
3. Remove local `paper/main.pdf` after export if the build script leaves it.
4. If the first rebuild asks for another LaTeX pass, rerun the canonical build
   and use only the final artifact metadata.
5. Recompute page count, SHA256, annotation colors, border widths, and link
   pages from the rebuilt PDF.
6. Render all affected link pages from the rebuilt Downloads PDF into
   `tmp/pdfs/paper23_after`.
7. Visually inspect the rendered affected pages:
   - green citation and URL boxes are crisp and aligned;
   - red internal-reference boxes are crisp and aligned;
   - no cyan boxes appear;
   - layout, figures, tables, headers, and page count remain stable.
8. Update README/status/audit/version/validation metadata with the new hash and
   visual-hardening result.
9. Scan LaTeX logs and build outputs for fatal errors, undefined
   citations/references, rerun warnings, and overfull boxes.
10. Remove Paper23 temp renders, leaving only the shared role-model render
    directory.
11. Stage only Paper23 source and metadata files, commit, push, and verify a
    clean repository.

## Non-Goals

- Do not alter experiment results, claims, figures, tables, bibliography
  content, or page count.
- Do not add or remove citations or URLs merely to change link counts.
- Do not leave intermediate PDFs or render folders behind.

## Completion Evidence

- Rebuilt Downloads artifact: `C:/Users/wangz/Downloads/23.pdf`
- Pages: 25
- Size: 360,190 bytes
- SHA256: `2605F94DB0B455CB5FCADB8887871887C8997C798EC2E90A7E73E3633082311B`
- Local `paper/main.pdf`: absent after export
- Link pages after rebuild:
  `[(2, 31), (5, 1), (6, 1), (8, 1), (12, 9), (13, 13)]`
- Annotation colors after rebuild: green = 53, red = 3, cyan = 0
- Border widths after rebuild: `(0, 0, 1)` for all 56 link annotations
- Rendered affected pages inspected from `tmp/pdfs/paper23_after`; green
  citation and URL boxes and red internal-reference boxes are crisp and aligned,
  and no cyan boxes are present.
