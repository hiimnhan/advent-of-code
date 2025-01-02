# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2022/day/6

from ...base import TextSolution, answer
import sys

sys.setrecursionlimit(10000)


class Solution(TextSolution):
    _year = 2022
    _day = 6

    @answer(1282)
    def part_1(self) -> int:
        ans = 0
        s = self.input

        for i in range(len(s) - 3):
            if len(set(s[i : i + 4])) == 4:
                return i + 4

        return ans

    @answer(3513)
    def part_2(self) -> int:
        ans = 0
        s = self.input

        for i in range(len(s) - 13):
            if len(set(s[i : i + 14])) == 14:
                return i + 14

        return ans
