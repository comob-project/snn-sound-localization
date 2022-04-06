# Script that
# 1) generates a table of contents for the website (`toc.yml`), and
# 2) builds the website (i.e. generate html) using jupyterbook (`jb`).
#
# To be run from the repo root.

import sys
import yaml
from subprocess import run

# Generate table of contents. See https://jupyterbook.org/structure/toc.html
toc = {
    format: "jb-book",

}

run(["jb", "build", "."], stdout=sys.stdout, stderr=sys.stderr)
    # Redirect stdout and stderr of this subprocess to the process running this script,
    # so that user sees the output of this command.
