# ▶ The Film — AI 2040 Plan A — design reference

This is a design mockup created in a visual design tool, exported as a
standalone page. Treat it as a REFERENCE MOCKUP, not production code:
the markup and inline styles carry the design's precise values — colors,
font sizes, spacing, radii, shadows, layout — which an implementation
should replicate faithfully in its own components and styling system
rather than copy wholesale.

## Contents

- `Main.dc.html` — the artboard (a Design Component: an `<x-dc>`
  template + a small logic class). The values to replicate live in its
  inline `style="…"` attributes and the `<helmet><style>` block.
- `AppM.dc.html` — referenced resource
- `AppN.dc.html` — referenced resource
- `AppQ.dc.html` — referenced resource
- `AppX.dc.html` — referenced resource
- `Branch.dc.html` — referenced resource
- `Compare.dc.html` — referenced resource
- `Credits.dc.html` — referenced resource
- `PlanAIntro.dc.html` — referenced resource
- `PlanB.dc.html` — referenced resource
- `PlanC.dc.html` — referenced resource
- `PlanD.dc.html` — referenced resource
- `PlanS.dc.html` — referenced resource
- `Timeline.dc.html` — referenced resource
- `Title.dc.html` — referenced resource
- `Y2027.dc.html` — referenced resource
- `Y2028.dc.html` — referenced resource
- `Y2029.dc.html` — referenced resource
- `Y2030.dc.html` — referenced resource
- `Y2031.dc.html` — referenced resource
- `Y2032.dc.html` — referenced resource
- `Y2033.dc.html` — referenced resource
- `Y2034.dc.html` — referenced resource
- `Y2035.dc.html` — referenced resource
- `Y2036.dc.html` — referenced resource
- `Y2037.dc.html` — referenced resource
- `Y2038.dc.html` — referenced resource
- `Y2039.dc.html` — referenced resource
- `Y2040.dc.html` — referenced resource
- `StatPanel.dc.html` — referenced resource
- `assets/` — files uploaded to the design (images, fonts, media)
- `support.js`, `vendor/react*.js` — the runtime that renders the
  component in a browser; not part of the design.

## Uploaded files

Images, fonts and media uploaded to the design are written once each under
`assets/` — 5 in this export — and the exported files refer to them there. A
reference a script puts together while the page runs (for example
`"/_blob/" + id`) is not rewritten and does not load from this folder.

## Viewing

Serve the folder (e.g. `python3 -m http.server`) and open `Main.dc.html`;
some browsers block the scripts over file://.
