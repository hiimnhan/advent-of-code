# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/24

from ...base import StrSplitSolution, answer
import sys
from collections import defaultdict

sys.setrecursionlimit(10000)


class Solution(StrSplitSolution):
    _year = 2024
    _day = 24

    separator = "\n\n"

    # @answer(1234)
    def part_1(self) -> int:
        d = defaultdict(int)
        initial = self.input[0]
        for l in initial.split("\n"):
            k, v = l.split(": ")
            d[k] = int(v)

        undefined = []

        opts = self.input[1]
        for l in opts.split("\n"):
            op, key = l.split(" -> ")
            a, b, c = op.split(" ")
            if a in d and c in d:
                if b == "AND":
                    d[key] = d[a] & d[c]
                if b == "OR":
                    d[key] = d[a] | d[c]
                if b == "XOR":
                    d[key] = d[a] ^ d[c]
            else:
                undefined.append(l)

        while undefined:
            for l in undefined:
                op, key = l.split(" -> ")
                a, b, c = op.split(" ")
                if a in d and c in d:
                    if b == "AND":
                        d[key] = d[a] & d[c]
                    if b == "OR":
                        d[key] = d[a] | d[c]
                    if b == "XOR":
                        d[key] = d[a] ^ d[c]
                    undefined.remove(l)
        a = sorted([k for k in d.keys() if k.startswith("z")], reverse=True)
        return int("".join([str(d[k]) for k in a]), 2)

    # @answer(1234)
    def part_2(self) -> int:
        ans = 0
        return ans
