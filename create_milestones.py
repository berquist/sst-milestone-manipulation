#!/usr/bin/env python

import argparse
import subprocess as sp
from pathlib import Path

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default="berquist/test-create-milestones")
    args = parser.parse_args()

    ret = sp.run(["gh", "extension", "install", "valeriobelli/gh-milestone"])

    __dir__ = Path(__file__).parent
    milestone_names = (__dir__ / "milestones.txt").read_text(encoding="utf-8").splitlines()

    for milestone_name in milestone_names:
        ret = sp.run(
            ["gh", "milestone", "create", "--title", milestone_name, "--repo", args.repo],
            capture_output=True,
        )
        stdout = ret.stdout.decode()
        if ret.returncode and "The milestone with the same title already exists." not in stdout:
            raise RuntimeError(stdout)
        print(stdout)
