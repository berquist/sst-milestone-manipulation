#!/usr/bin/env python

import subprocess as sp
from pathlib import Path

if __name__ == "__main__":
    ret = sp.run(["gh", "extension", "install", "valeriobelli/gh-milestone"])

    __dir__ = Path(__file__).parent
    milestone_names = (__dir__ / "milestones.txt").read_text(encoding="utf-8").splitlines()

    REPO = "berquist/test-create-milestones"

    for milestone_name in milestone_names:
        ret = sp.run(
            ["gh", "milestone", "create", "--title", milestone_name, "--repo", REPO],
        )
