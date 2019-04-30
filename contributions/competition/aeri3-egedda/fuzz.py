from util import Util
from fractions import Fraction

import os
import sys

COREUTILS = [
 #   "cat",
    "cp",
    "date",
  #  "dd",
    "df",
    "dir",
    "echo",
    "false",
    "ln",
    "ls",
    "mkdir",
    "mktemp",
    "mv",
    "pwd",
    "sleep",
    "printf",
    "touch",
    "true",
    "uname",
    "vdir"
]

def writeLinesToFile(lines, path):
    # print("[h4xfuzz] writing lines to '{}'".format(path))
    with open(path, "a") as f:
        for line in lines:
            f.write(' '.join(line) + "\n")

def addCustomLines(util_name):
    lines = set()
    path = "data/custom_lines/{}.txt".format(util_name)
    try:
        with open(path) as f:
            for line in f:
                lines.add("{} {}".format(util_name, line.strip()))
        return lines
    except FileNotFoundError:
        print("[h4xfuzz] no custom lines found for '{}' at '{}'".format(util_name, path))
        return lines


if __name__ == '__main__':
    print("[h4xfuzz] h4xfuzz started")
    lines = set()
    covered_lines = 0
    total_lines = 1
    above_50 = 0
    for util_name in COREUTILS:
        lines = set()
        util = Util(util_name)
        print("[h4xfuzz] Fuzzing {}...".format(util.name))
        for _ in range(1000):
            args = util.fuzz()
            writeLinesToFile(args, "out/{}.txt".format(util_name))
            for cli in args:
                util.execute(cli)

        util_cov = util.getCoverage()
        util_covered_lines = util_cov[0]
        util_total_lines = util_cov[1]
        covered_lines += util_covered_lines
        total_lines += util_total_lines
        if util_covered_lines == 0:
            util_total_lines = 1
        print("[h4xfuzz] {}: {}%".format(util_name, float(round(util_covered_lines / util_total_lines, 4) * 100)))
        if util_covered_lines / util_total_lines >= 0.5:
            above_50 += 1

    print("\nTotal coverage: {}%".format(float(round(covered_lines / total_lines, 4) * 100)))
    print("\nUtils above 50% coverage: {}".format(above_50))
    if sys.argv[1]:
        writeLinesToFile(lines, sys.argv[1])
