# Script that
# 1) modifies the config and table of contents for the website; and
# 2) builds the website (i.e. generate html) using jupyterbook (`jb`).
#
# To be run from the repo root (i.e. the same directory that contains `notebooks/`).


from util import read, write, run

from pathlib import Path
from shutil import rmtree



# -----------------
# Define directories

reporoot = Path.cwd()
nbdir = reporoot / "notebooks"
webdir = reporoot / "web"
outdir = webdir / "_generated"
rmtree(outdir, ignore_errors=True)
# Delete leftovers from previous builds. These cause confusion when debugging
# manually. Error is raised when outdir does not exist.
outdir.mkdir()



# ------------------------------
# Complete the table of contents

toc = read(webdir / "_toc.yml")


def to_toc_entry(p: Path):
    # See the incomplete _toc.yml for expected syntax
    return {"file": p.relative_to(reporoot).with_suffix("").as_posix()}

toc["chapters"] = [to_toc_entry(nbpath) for nbpath in nbdir.glob("*.ipynb")]

tocfile = outdir / "_toc__completed.yml"
write(toc, tocfile)




# -------------------------------
# Complete the JupyterBook config

config = read(webdir / "_config.yml")

config["repository"]["branch"] = "main"

configfile = outdir / "_config__completed.yml"
write(config, configfile)




# -------------
# Generate html

run(
    f"jb build ."
    f" --path-output {outdir}"  # (creates "_build" subdir automatically).
    f" --toc {tocfile}"
    f" --config {configfile}"
)
