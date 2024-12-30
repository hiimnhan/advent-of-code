# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2022/day/3

from solutions.utils.algo import common_chars
from ...base import StrSplitSolution, answer
import sys

sys.setrecursionlimit(10000)


class Solution(StrSplitSolution):
    _year = 2022
    _day = 3

    @answer(7980)
    def part_1(self) -> int:
        ans = 0
        for line in self.input:
            a = line[: len(line) // 2]
            b = line[len(line) // 2 :]
            for aa in a:
                if aa in b:
                    if aa.islower():
                        ans += ord(aa) - 96
                    else:
                        ans += ord(aa) - 38
                    break
        return ans

    @answer(2881)
    def part_2(self) -> int:
        ans = 0
        N = len(self.input)

        for i in range(0, N, 3):
            a, b, c = self.input[i], self.input[i + 1], self.input[i + 2]
            common = common_chars([a, b, c])
            aa = common[0]
            if aa.islower():
                ans += ord(aa) - 96
            else:
                ans += ord(aa) - 38

        return ans
