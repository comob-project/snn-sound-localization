# SNN Sound Localization

Training spiking neural networks for sound localization

## Workflow

A detailed description can be found in the `CONTRIBUTING.md` file. Briefly, the `notebooks/` directory is a
free-for-all, just try to keep your work in your own notebook to avoid conflicts. When you have a polished piece of work
(e.g. to generate a figure for the paper), open a pull request to add it to the `spikeloc/` directory where the "finished"
code lives. Code must be reviewed before being merged into `spikeloc/`.

If you need help with using git/Github, just ask in the discord and someone will lend a hand!

## Installation

Multiple installation methods are supported: conda (environment.yml), poetry (pyproject.toml), pip
(requirements.txt), docker (DOCKERFILE)

### Conda

1. `conda env create -f environment.yml`
2. `conda activate spikeloc`

### Poetry

1. Install [Poetry](https://python-poetry.org/)
2. (optional) Create a virtualenv: `python -m venv .venv`
3. (optional) Source the newly created virtualenv: `source .venv/bin/activate`
4. Run `poetry install`

### Pip

1. Create a virtualenv: `python -m venv .venv`
2. Source the newly created virtualenv: `source .venv/bin/activate`
3. Run `pip install -r requirements.txt`

## Community

Find us on Discord [here](https://discord.gg/Zpd6RYYyuf)
