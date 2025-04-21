# COMOB · SNN Sound Localization project 🎧

This is the repository behind the _SNN Sound Localization_ project. Check out [the website](https://comob-project.github.io/snn-sound-localization/) for more information about the project and how to join and contribute.


## Contents

- `research/`: Jupyter Notebooks and markdown files with research notes, code, and plots. Gets built into the website.
- `paper/`: Markdown files with the paper in progress. Also gets built into the website.
- `index.md`: Home page ("About") of the website
- `environment.yml`: conda environment to run the notebooks in `research/`.

## Dev notes

To edit and build locally, [install node and myst following these instructions](https://mystmd.org/guide/quickstart).

To edit locally:

```
myst start
```

Then click the link in the terminal (probably ``http://localhost:3000``).

### LaTeX build

At the moment, the typst build has some problems with equations. Use

```
myst build paper/paper.md --tex
```

and then you need to edit the generated latex in ``_build/exports/paper_tex`` as follows:

1. Change first line to ``\documentclass[a4paper,11pt]{article}``. This is because we use the book preprint from mystmd as it works best at time of writing, but we don't want a book.
2. Remove the ``\frontmatter`` and ``\mainmatter`` commands because it's not a book.
3. Remove the formatting if desired from ``\title`` and ``\author``.
4. Replace commas and ``and`` in the ``author{}`` with ``\and`` to spread across multiple lines correctly.
5. For each section authors table, add ``[!h]`` to the end of the table declaration otherwise it puts it at the top of the page.
6. Remove ``\tableofcontents``
7. Add ``\begin{abstract}`` and ``\end{abstract}`` around the abstract.
8. Remove the table in the contributors section and replace it with the following text: "Full list of contributions available online at \url{https://comob-project.github.io/snn-sound-localization/paper\#contributors}."

It should then build with a standard ``pdlatex-bibtex-pdflatex*2`` build.