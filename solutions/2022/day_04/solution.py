# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2022/day/4

from solutions.utils.algo import is_contain, is_overlap
from ...base import StrSplitSolution, answer
import sys

sys.setrecursionlimit(10000)


class Solution(StrSplitSolution):
    _year = 2022
    _day = 4

    def gen(self, input):
        a, b = input.split(",")
        aa, aaa = map(int, a.split("-"))
        bb, bbb = map(int, b.split("-"))
        return aa, aaa, bb, bbb

    # @answer(1234)
    def part_1(self) -> int:
        ans = 0
        for line in self.input:
            a, b, c, d = self.gen(line)
            if is_contain(a, b, c, d) or is_contain(c, d, a, b):
                ans += 1
        return ans

    # @answer(1234)
    def part_2(self) -> int:
        ans = 0
        for line in self.input:
            a, b, c, d = self.gen(line)
            if is_overlap(a, b, c, d) or is_overlap(c, d, a, b):
                ans += 1
        return ans
