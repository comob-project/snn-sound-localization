# Script that
# 1) modifies the config and table of contents (toc) for the website; and
# 2) builds the website (i.e. generate html) using jupyterbook (`jb`).
#
# To be run from the repo root (i.e. the same directory that contains `notebooks/`).


from util import read, write, run  # local helper functions

from pathlib import Path
from shutil import rmtree
from os import environ



# -----------------
# Define directories

reporoot = Path.cwd()
nbdir = reporoot / "notebooks"
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
    # To generate yaml output of the form "- notebooks/introduction".
    return {"file": p.relative_to(reporoot).with_suffix("").as_posix()}

toc["chapters"] = [to_toc_entry(nbpath) for nbpath in nbdir.glob("*.ipynb")]

write(toc, tocfile := outdir / "_toc__completed.yml")




# -------------------------------
# Complete the JupyterBook config

config = read(webdir / "_config.yml")

config["repository"]["branch"] = environ.get("GITHUB_REF_NAME", "unknown-branch")
# If we're not running on Githhub Actions (i.e. testing locally), we don't bother
# getting the current branch name [we could, by calling `git`].
# Env var from
# https://docs.github.com/en/actions/learn-github-actions/environment-variables

write(config, configfile := outdir / "_config__completed.yml")



# -------------
# Generate html

run(
    f"jb build ."
    f" --path-output {outdir}"  # (creates "_build" subdir automatically).
    f" --toc {tocfile}"
    f" --config {configfile}"
)
