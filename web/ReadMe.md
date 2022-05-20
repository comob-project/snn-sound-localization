
## What is this?

This directory contains configuration and code to generate web pages
(hosted [here](https://comob-project.github.io/snn-sound-localization/))
based on content in this repository (most notably the Jupyter Notebooks in `../notebooks/`).

This conversion into HTML is done using [JupyterBook](https://jupyterbook.org/)
(which is [based on](https://jupyterbook.org/explain/sphinx.html)
the [Sphinx](https://www.sphinx-doc.org) HTML generator).  


<br>

## Automatic build with GitHub Actions

A GitHub computer automatically builds a JupyterBook website
(by running [`build.py`](build.py)) for every branch,
on every push to that branch on GitHub.

This process is defined in 
[`../.github/workflows/deploy-web.yml`](../.github/workflows/deploy-web.yml)


<br>

## How to build the website locally

You need `conda`.
The recommended way to install conda is [Miniforge](https://github.com/conda-forge/miniforge).

To download the software used for building the website, run, from the repo root:
```
conda env create -f web/conda-environment.yml
```

To then build the website, activate the newly created conda environment:
```
conda activate comob-soundloc-web
```
Then, still in the repo root, run
```
python web/build.py
```
When the build is complete, you'll get a link to view the local build in the browser.
