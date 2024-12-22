# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/21

from ...base import StrSplitSolution, answer
import sys

sys.setrecursionlimit(10000)


class Solution(StrSplitSolution):
    _year = 2024
    _day = 21

    number_pad = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [None, 0, -1]]

    arrow_pad = [
        [None, "^", "A"],
        ["<", "v", ">"],
    ]

    # @answer(1234)
    def part_1(self) -> int:
        ans = 0
        return ans

    # @answer(1234)
    def part_2(self) -> int:
        ans = 0
        return ans
