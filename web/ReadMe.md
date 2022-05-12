
## What is this?

This directory contains configuration files and code to convert the content in this repository
(most notably the Jupyter Notebooks in `../notebooks/`) 
into html, to be hosted on the web.

This is done using '[JupyterBook](https://jupyterbook.org/)'
(which [is based on](https://jupyterbook.org/explain/sphinx.html)
the '[Sphinx](https://www.sphinx-doc.org)' html generator).
It is a Python package
([`jupyter-book`](https://github.com/executablebooks/jupyter-book))
that we install using conda.

A GitHub computer automatically builds a JupyterBook website
(by running [`build.py`](build.py)) for every branch,
on every push to that branch on GitHub.

These JupyterBooks are hosted at https://comob-project.github.io/snn-sound-localization/

The configuration of this automatic building is at
[`../.github/workflows/deploy-web.yml`](../.github/workflows/deploy-web.yml).



## How to build the website locally

You need `conda`.
The recommended way to install conda is [Miniforge](https://github.com/conda-forge/miniforge).

To create the conda environment in which the website is built, run, from the repo root:
```
conda env create -f web/conda-environment.yml
```

To build the website, activate this new environment:
```
conda activate comob_soundloc_build-jb-website
```
Then, still in the repo root, run
```
python web/build.py
```
The output of this command will give the link to open in your browser
to view the locally built website.
