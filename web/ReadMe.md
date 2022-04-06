This directory contains config and code to convert content in this repository
(most notably the Jupyter Notebooks in `../notebooks/`) 
into html, to be hosted on the web.

This is done using [`JupyterBook`](https://jupyterbook.org/)
(which [is based on](https://jupyterbook.org/explain/sphinx.html)
the [Sphinx](https://www.sphinx-doc.org) html generator).
It is a Python package
([`jupyter-book`](https://github.com/executablebooks/jupyter-book))
that we install using conda.
The recommended way to install conda is [Miniforge](https://github.com/conda-forge/miniforge).

To create the conda environment in which the website is built, run, from the repo root:
```
conda env create -f web/conda-environment.yml
```

To build the website, activate this new environment:
```
conda activate comob-soundloc-jb
```

Then, still in the repo root, run
```
python web/build.py
```
