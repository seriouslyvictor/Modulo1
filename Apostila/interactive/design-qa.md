# Design QA — Interactive Apostila, Chapters 1–4

- Source visual truth: `C:\Users\besto\.codex\generated_images\019f8cb5-7523-7782-b9cc-ed4c19b44559\exec-f5ab7d91-8435-4576-afcf-2924b8945f5c.png`
- Final implementation screenshot: `D:\Modulo1\Apostila\interactive\implementation-qa-pass2.png`
- Final side-by-side evidence: `D:\Modulo1\Apostila\interactive\design-qa-comparison-pass2.png`
- Requested CSS viewport: 1440 × 1024
- Source pixels: 1487 × 1058
- Implementation pixels: 1425 × 1013
- Density normalization: source resized to 1425 × 1013 with high-quality bicubic interpolation for the side-by-side comparison; implementation remained at native capture size.
- State: desktop, Chapter 3, “Convertendo valores”, current lesson group open, 0% chapter progress.

## Full-view comparison evidence

The final comparison preserves the selected model’s three-region composition: warm chapter rail, focused white reading surface, and quiet contextual-help rail. The implementation maintains the source hierarchy, sparse red accent, rounded controls, flat surfaces, sticky lesson navigation, visible progress, and strong primary continuation action.

The implementation intentionally uses the full canonical Chapter 3 content rather than the abbreviated mock content. The section number, exact copy, content height, and number of lesson steps therefore differ from the generated source while preserving its interaction and layout model.

## Focused region comparison

A separate crop was not required. The original-pixel side-by-side evidence keeps the chapter rail, heading, code surface, contextual-help rail, typography, and spacing legible enough to evaluate the required fidelity surfaces.

## Required fidelity surfaces

- Fonts and typography: Inter-compatible system stack, readable 17px lesson copy, restrained UI sizes, clear heading hierarchy, and monospace code. Heading scale and line length match the source intent. Passed.
- Spacing and layout rhythm: stable three-column desktop frame, bounded reading column, generous whitespace, 16px control radii, minimal elevation, and responsive mobile conversion. Passed.
- Colors and visual tokens: temporary warm neutral/red palette is isolated behind CSS custom properties and stays consistent with the source. Contrast and keyboard focus treatment are clear. Passed.
- Image quality and asset fidelity: the selected source contains no photography or bespoke illustration. All interface icons use the Phosphor icon library; no placeholder imagery, CSS drawings, inline SVGs, emoji, or text-glyph substitutes were introduced. Passed.
- Copy and content: all visible instructional content comes from the existing Portuguese Markdown sources. Navigation labels and progress copy are concise and correctly accented. Passed.

## Browser verification

Browser-rendered checks completed in the Codex in-app browser:

- completed a section and advanced to the next one;
- reloaded and confirmed section progress and last location were preserved;
- transitioned from the last section of Chapter 1 to Chapter 2;
- opened a progressive hint in Chapter 3;
- triggered code-copy success feedback;
- opened the responsive chapter drawer at 390 × 844;
- transitioned from Chapter 3 into Chapter 4;
- rendered all 23 Chapter 4 sections from its canonical Markdown source;
- loaded the Chapter 4 starter manifest and exposed its verified ZIP download;
- checked the Chapter 4 starter card at 390 × 844 with no horizontal overflow;
- checked the final page in a fresh tab with no console errors or warnings.

## Comparison history

### Pass 1

- [P2] The 21-section rail was presented as one flat list and the Chapter 3 title was abbreviated.
  - Evidence: `design-qa-comparison-pass1.png`
  - Impact: the rail felt denser and harder to scan than the selected source, particularly for a beginner.
  - Fix: grouped sections into “Comece aqui”, “Conceitos”, “Prática”, and “Revisão e fechamento”; only the current group opens by default. Restored the full chapter title.

### Pass 2

- Evidence: `design-qa-comparison-pass2.png`
- Result: the staged rail restores clear hierarchy while keeping every canonical Markdown section directly reachable. No actionable P0, P1, or P2 mismatch remains.

## Follow-up polish

- [P3] Add lightweight syntax highlighting after the learning-flow validation if students find monochrome code harder to scan.
- [P3] Replace the temporary CSS token values with official SENAI tokens when they are available.
- [P3] Consider lazy-loading the Markdown rendering layer when optimizing beyond prototype scale; the current production bundle is functional but emits Vite’s large-chunk advisory.

final result: passed
