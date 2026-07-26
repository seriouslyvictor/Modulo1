# Prototype Instructions

Run the local server yourself and open the preview in the browser available to this environment. Do not give the user server-start instructions when you can run it.

Before making substantial visual changes, use the Product Design plugin's `get-context` skill when the visual source is unclear or no longer matches the current goal. When the user gives durable prototype-specific design feedback, preferences, or decisions, record them in `AGENTS.md`.

When implementing from a selected generated mock, treat that image as the source of truth for layout, component anatomy, density, spacing, color, typography, visible content, and hierarchy.

Build app UI in `src/`. Keep `.openai/hosting.json`, `worker/index.js`, `scripts/prepare-sites-build.mjs`, and `tests/sites-worker.test.mjs` intact so the same local prototype can be handed to Sites. Before a Sites handoff, run `pnpm build` and `pnpm test:sites`; the build must leave `dist/client/index.html`, `dist/server/index.js`, and `dist/.openai/hosting.json`.

## Prototype decisions

- Optimize for learning clarity and beginner confidence before visual polish.
- Use the selected "Guided Chapter Rail" mock as the structural source of truth.
- Build every canonical chapter currently available (1–12) and keep each
  chapter's existing Markdown file as the content source of truth.
- Use the Pinterest-derived warm neutral/red system only as temporary scaffolding; keep visual values behind CSS custom properties so official SENAI tokens can replace them later.
- Use a client-only React + TypeScript + Vite architecture. Store progress locally for this validation pass; do not add accounts, a backend, a database, or an embedded Python runtime.
