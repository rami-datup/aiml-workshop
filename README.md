# aiml-workshop

Hands-on learning material for an **AI / Machine Learning workshop**: slide decks, animations and a
sequence of Google Colab labs that take you from a neural network written in NumPy to modern
time-series forecasting models.

- **Decks**: the course presentation, split by topic, with speaker notes, plus the "The Film — AI 2040 Plan A" deck.
- **Labs (L0 to L5)**: Jupyter notebooks designed to run in **Google Colab**, with no manual uploads
  and no Google Drive mounting. Each lab sets up its own helper files and data.

---

## Repository structure

```
aiml-workshop/
├── decks/                         Slide decks, one self-contained folder per deck
│   ├── Course Presentation/             course hub (HTML) and full deck (PDF)
│   ├── Intro & Motivation/              slides, images and the Week 1 .pptx source
│   ├── Neural Network Implementation/
│   ├── Activation Functions/
│   ├── Regularization, Bias and Variance/
│   ├── Advanced Neural Networks/
│   ├── ▶ The Film — AI 2040 Plan A-html/   "AI 2040 Plan A" film deck (Main.dc.html is the entry point)
│   └── README.md                        what is in each folder and how to view the decks
├── labs/
│   ├── L0. Neural Network from Scratch/
│   ├── L1. Neural Network/
│   ├── L2. Binary Classification/
│   ├── L3. Activation Functions/
│   ├── L4. Bias vs Variance/
│   └── L5. Advanced Neural Networks/
├── LICENSE                        MIT
└── README.md
```

Each lab folder contains its notebook(s) plus whatever the notebook needs next to it: helper modules
(`utils.py`, `autils.py`, `lab_*_utils.py`, `public_tests.py`), the plotting style
(`deeplearning.mplstyle`), and `data/` or `images/` where applicable.

### Labs

| Lab | Title | What you do | Runtime | Open |
|---|---|---|---|---|
| **L0.1** | Neural Network with 2 Layers | Build and train a two-layer neural network from scratch in NumPy (forward and backward propagation) to solve a classification problem. | CPU | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rami-datup/aiml-workshop/blob/main/labs/L0.%20Neural%20Network%20from%20Scratch/L0.1%20Neural%20Network%20with%202%20Layers.ipynb) |
| **L1.1** | Neurons and Layers | Neurons and layers in TensorFlow/Keras: a single neuron as linear and logistic regression, then a layer of neurons. | CPU | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rami-datup/aiml-workshop/blob/main/labs/L1.%20Neural%20Network/L1.1%20Neurons%20and%20Layers.ipynb) |
| **L1.2** | Coffee Roasting in Tensorflow | A first end-to-end Keras network (coffee roasting): normalization, training, prediction. | CPU | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rami-datup/aiml-workshop/blob/main/labs/L1.%20Neural%20Network/L1.2%20Coffee%20Roasting%20in%20Tensorflow.ipynb) |
| **L2.1** | NN Binary Classification | Handwritten digit recognition, binary (0 vs 1), with a small dense network. | CPU | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rami-datup/aiml-workshop/blob/main/labs/L2.%20Binary%20Classification/L2.1%20NN%20Binary%20Classification.ipynb) |
| **L3.1** | NN Digits Recognition | ReLU and softmax; multiclass digit recognition (0-9) with a three-layer network. | CPU | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rami-datup/aiml-workshop/blob/main/labs/L3.%20Activation%20Functions/L3.1%20NN%20Digits%20Recognition.ipynb) |
| **L4.1** | Diagnose Bias and Variance | Baselines, learning curves and regularization (Ridge) to diagnose high bias vs high variance. | CPU | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rami-datup/aiml-workshop/blob/main/labs/L4.%20Bias%20vs%20Variance/L4.1%20Diagnose%20Bias%20and%20Variance.ipynb) |
| **L4.2** | Evaluation and Selection | Train/CV/test splits and model selection for polynomial regression, neural networks and classification. | CPU | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rami-datup/aiml-workshop/blob/main/labs/L4.%20Bias%20vs%20Variance/L4.2%20Evaluation%20and%20Selection.ipynb) |
| **L5.1** | Temporal Fusion Transformer | Demand forecasting with the Temporal Fusion Transformer on the Stallion dataset (PyTorch Forecasting). About 13 min on CPU. | CPU (GPU optional) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rami-datup/aiml-workshop/blob/main/labs/L5.%20Advanced%20Neural%20Networks/L5.1%20Temporal%20Fusion%20Transformer.ipynb) |
| **L5.2** | Chronos-2 | Getting started with Chronos-2, a pretrained time-series model: univariate forecasting and forecasting with covariates (e.g. energy prices). | GPU required | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rami-datup/aiml-workshop/blob/main/labs/L5.%20Advanced%20Neural%20Networks/L5.2%20Chronos-2.ipynb) |

> The links above open the notebooks straight from GitHub. This repository is **public**, so the badges
> work for anyone — no fork or GitHub account required. [Fork it](#3-fork-the-repo-optional) only if you
> want to save your own changes.

### Decks

Open `decks/Course Presentation/Course Presentation.pdf` for the full deck. The `.dc.html` decks need a local web
server (a page opened straight from disk may not run). Start at the course hub, which links to each lecture:

```bash
cd decks
python3 -m http.server      # then open http://localhost:8000/Course%20Presentation/Course%20Presentation.dc.html
```

The **AI 2040 Plan A** deck lives in its own folder, `decks/▶ The Film — AI 2040 Plan A-html/`. Serve that
folder the same way and open `Main.dc.html` (a timeline of per-year pages, `Y2027` to `Y2040`, and the
Plan A to D branches).

---

## Getting started

You need a Google account to run the labs in Colab; nothing has to be installed locally. A GitHub account
is only needed if you want your own fork (for example to save and share your changes).

### 1. Open a notebook in Colab

Click an **Open in Colab** badge in the [Labs](#labs) table, or open <https://colab.research.google.com>,
choose **File → Open notebook → GitHub**, pick `rami-datup/aiml-workshop` and `main`, and select a
notebook under `labs/`.

The repository is public, so Colab can open it without signing in to GitHub.

Or build the URL yourself: take any notebook's GitHub path and prefix it with
`https://colab.research.google.com/github/`, with spaces written as `%20`. For example:

```
https://colab.research.google.com/github/rami-datup/aiml-workshop/blob/main/labs/L4.%20Bias%20vs%20Variance/L4.1%20Diagnose%20Bias%20and%20Variance.ipynb
```

### 2. Run a lab

1. Choose the runtime: **Runtime → Change runtime type**. Most labs run on CPU. **L5.2 (Chronos-2)
   needs a GPU runtime** (it loads the model with `device_map="cuda"`).
2. Run the **first cell**. It installs missing packages (L5) or clones the repo and moves into the lab
   folder (L0 to L4). Expect a `Lab folder: ...` line as output.
3. Run the rest of the notebook with **Runtime → Run all**, or cell by cell with Shift+Enter.
   If Colab asks you to restart the runtime after an install, do that and run again from the top.

### 3. Fork the repo (optional)

Do this only if you want your own copy — for example to edit the notebooks and keep your changes in your
own GitHub account. The badges above and the setup cells work against the upstream repo as-is.

**Using the web UI**

1. Sign in to GitHub and open `https://github.com/rami-datup/aiml-workshop`.
2. Click **Fork** (top right), choose your account as the owner, keep the name `aiml-workshop`, and click
   **Create fork**.

**Using the GitHub CLI**

```bash
gh repo fork rami-datup/aiml-workshop --clone     # forks into your account and clones it
```

You now have `https://github.com/<your-username>/aiml-workshop`. A fork of a public repo is public by
default.

#### Point the notebooks at your fork

The labs that ship helper files (L0 to L4) start with a **setup cell**. In Colab the notebook file is
loaded on its own, so the cell clones the repo into `/content/aiml-workshop` and adds the lab folder to
`sys.path`. When it runs on your own machine inside the repo, it skips the clone.
It clones from the URL in this line:

```python
REPO_URL = "https://github.com/rami-datup/aiml-workshop.git"
```

If you changed helper files or notebooks in your fork, change `rami-datup` to **your** GitHub username so
the setup cell pulls your version. To update every notebook at once, run this from the repo root (macOS:
use `sed -i ''`):

```bash
git clone https://github.com/<your-username>/aiml-workshop.git && cd aiml-workshop
grep -rlZ "rami-datup/aiml-workshop" labs --include=*.ipynb \
  | xargs -0 sed -i 's#rami-datup/aiml-workshop#<your-username>/aiml-workshop#g'
git commit -am "Point labs to my fork" && git push
```

#### Private fork? Give Colab a token (rarely needed)

A fork of a public repo is public, so this only applies if you changed your fork's visibility to private.
A private fork cannot be cloned anonymously, so create a read-only token and store it as a Colab secret.
The setup cell looks for a secret named `GH_TOKEN`.

1. GitHub, then **Settings → Developer settings → Personal access tokens → Fine-grained tokens →
   Generate new token**.
2. Repository access: **Only select repositories**, choose your fork. Permissions: **Contents → Read-only**.
3. Copy the token. In Colab, open the **key icon (Secrets)** in the left sidebar, then **Add new secret**:
   name `GH_TOKEN`, value the token, and switch on **Notebook access**.

To save your work back to GitHub: **File → Save a copy in GitHub**, choose your fork, and commit.

**Troubleshooting**

| Symptom | Fix |
|---|---|
| `fatal: could not read Username` / repository not found during the clone | `REPO_URL` points to a repo you cannot access: use the public upstream URL, or if the fork is private add the `GH_TOKEN` secret and check `REPO_URL`. |
| `ModuleNotFoundError: utils` (or `autils`, `w3_unittest`) | The setup cell did not run. Run it first, then re-run the failing cell. |
| Plot styling errors about `deeplearning.mplstyle` | Same cause: the notebook must run inside its lab folder, which the setup cell sets up. |
| L5.1 install cell says restart required | Restart the runtime, then run from the top. |

**Running locally instead** (optional): clone the repo, create a Python 3.10+ virtual environment, install
what the lab imports (`numpy`, `matplotlib`, `scikit-learn`, `tensorflow` for L1 to L4; see the install
cell at the top of each L5 notebook), start Jupyter **from inside the lab folder** so that helper files
and `data/` resolve, and run the notebook.

---

## Credits

- L0 to L4 are adapted from the practice labs of the DeepLearning.AI Machine Learning courses.
- L5.1 reproduces the [PyTorch Forecasting Stallion tutorial](https://pytorch-forecasting.readthedocs.io/en/stable/tutorials/stallion.html).
- L5.2 follows the getting-started notebook of [Chronos-2](https://github.com/amazon-science/chronos-forecasting).

## License

[MIT](LICENSE). Third-party datasets, course material and the libraries used by the labs keep their own licenses.

## Contact

Maintainer: **Rami** ([@rami-datup](https://github.com/rami-datup)).

- Questions, bugs or suggestions: open an [issue](https://github.com/rami-datup/aiml-workshop/issues) on GitHub.
- The repository is public, so you can read, fork and reuse it under the [license](#license).
