# Script that
# 1) modifies the config and table of contents (toc) for the website; and
# 2) builds the website (i.e. generate html) using jupyterbook (`jb`).
#
# To be run from the repo root (i.e. the same directory that contains `notebooks/`).


from util import read, write, run  # local helper functions

from pathlib import Path
from shutil import rmtree


# -----------------
# Define directories

reporoot = Path.cwd()
contentdir = reporoot / "research"
webdir = reporoot / "web"
outdir = webdir / "_generated"

if outdir.exists():
    rmtree(outdir)
    # Delete leftovers from previous builds.
    # These cause confusion when debugging manually.
    print(f"Cleared {outdir}")

outdir.mkdir()


# ------------------------------
# Complete the table of contents

toc = read(webdir / "_toc.yml")


def to_toc_entry(p: Path):
    # To generate yaml output of the form "- file: research/Starting-Notebook".
    return {"file": p.relative_to(reporoot).with_suffix("").as_posix()}


# Add notebooks and markdown files in "Research" to the "Research" part of toc..
#  - ..if they're not already there (like Background.md)
#  - ..sorted with most recently edited first

research_toc = toc["parts"][1]["chapters"]

all_content_files = [p for p in contentdir.iterdir() if p.suffix in (".ipynb", ".md")]
new_content_files = [
    p for p in all_content_files if to_toc_entry(p) not in research_toc
]
last_modified_first = sorted(
    new_content_files, key=lambda p: p.stat().st_mtime, reverse=True
)
    # More recently modified files have larger (later) mtimes, and must come first.
research_toc += [to_toc_entry(p) for p in last_modified_first]

write(toc, tocfile := outdir / "_toc__completed.yml")


# -------------
# Generate html

run(
    f"jb build ."
    f" --path-output {outdir}"  # (creates "_build" subdir automatically).
    f" --toc {tocfile}"
    f" --config {webdir / '_config.yml'}"
)
