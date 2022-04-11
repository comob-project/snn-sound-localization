import sys
import yaml
import subprocess

def read(yamlfile):
    with open(yamlfile) as f:
        obj = yaml.safe_load(f)
    return obj

def write(obj, yamlfile):
    with open(yamlfile, "w") as f:
        yaml.safe_dump(obj, f)

def run(cmd: str):
    subprocess.run(cmd.split(" "), stdout=sys.stdout, stderr=sys.stderr)
    # Propagate subprocess's output streams up, so that the user of this script sees
    # e.g. JupyterBook's build log.
