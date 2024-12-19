# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/19

from ...base import StrSplitSolution
import sys

sys.setrecursionlimit(10000)


class Solution(StrSplitSolution):
    _year = 2024
    _day = 19

    separator = "\n\n"

    # @answer(1234)
    def part_1(self) -> int:
        ans = 0
        pattern = set([x for x in self.input[0].split(", ")])
        towels = [x for x in self.input[1].split("\n") if x]

        for t in towels:
            n = len(t)
            dp = [False] * (n + 1)
            dp[0] = True

            for i in range(n):
                if dp[i]:
                    for p in pattern:
                        if t[i : i + len(p)] == p:
                            dp[i + len(p)] = True
            if dp[n]:
                ans += 1

        return ans

    # @answer(1234)
    def part_2(self) -> int:
        ans = 0
        pattern = set([x for x in self.input[0].split(", ")])
        towels = [x for x in self.input[1].split("\n") if x]

        for t in towels:
            n = len(t)
            dp = [0] * (n + 1)
            dp[0] = 1

            for i in range(n):
                if dp[i] > 0:
                    for p in pattern:
                        if t[i : i + len(p)] == p:
                            dp[i + len(p)] += dp[i]
            ans += dp[n]
        return ans
