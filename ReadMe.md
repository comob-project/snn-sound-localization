# COMOB · SNN Sound Localization project 🎧

This is the repository behind the _SNN Sound Localization_ project. Check out [the website](https://comob-project.github.io/snn-sound-localization/) for more information about the project and how to join and contribute.

[Current version of the paper (pdf)](https://github.com/comob-project/snn-sound-localization/releases/download/latest/paper.pdf) if build ran without error.


## Contents

- `research/`: Jupyter Notebooks and markdown files with research notes, code, and plots. Gets built into the website.
- `web/`: Code and config to build the website.
- `index.md`: Home page ("About") of the website
- `environment.yml`: conda environment to run the notebooks in `research/`.

## Dev notes

To edit and build locally, [install node and myst following these instructions](https://mystmd.org/guide/quickstart).

To build the paper, run the following from the root directory:

```
myst build paper/paper.md --pdf
```

To edit locally:

```
myst start
```

Then click the link in the terminal (probably ``http://localhost:3000``).