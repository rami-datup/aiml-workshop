# Decks

One folder per deck. Each folder is self-contained (its own `support.js`, media and sources), so a
folder can be served or copied on its own.

| Folder | Entry point | Also contains |
|---|---|---|
| `Course Presentation/` | `Course Presentation.dc.html` (course hub: syllabus, objectives, labs, links to the lectures) | `Course Presentation.pdf` (full deck, PDF) |
| `Intro & Motivation/` | `Intro & Motivation.dc.html` | `deck-stage.js`, `pptx_media/` (slide images), `uploads/Week 1 - AI and SocialTech.pptx` (source deck), `slide_content.txt`, `notes_content.txt`, `slide_image_map.txt` (text extracted from the .pptx) |
| `Neural Network Implementation/` | `Neural Network Implementation.dc.html` | `uploads/` (the lecture page it embeds) |
| `Activation Functions/` | `Activation Functions.dc.html` | `uploads/` |
| `Regularization, Bias and Variance/` | `Regularization, Bias and Variance.dc.html` | `uploads/` |
| `Advanced Neural Networks/` | `Advanced Neural Networks.dc.html` | `uploads/` |
| `▶ The Film — AI 2040 Plan A-html/` | `Main.dc.html` | see its own `README.md` |

The `Course Presentation` hub links to the other lectures with relative paths (`../<deck>/<deck>.dc.html`),
so keep the folders side by side.

In each `uploads/` folder the file with a hash suffix (for example `Activation Functions-163df51e.html`) is the one
the wrapper loads; the file without the suffix is an identical copy.

## Viewing

The `.dc.html` pages need a local web server (a page opened straight from disk may not run). Serve this
folder and open a deck through it:

```bash
cd decks
python3 -m http.server      # then open http://localhost:8000/Course%20Presentation/Course%20Presentation.dc.html
```
