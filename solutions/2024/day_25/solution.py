# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/25

from ...base import StrSplitSolution, answer
import sys

sys.setrecursionlimit(10000)


class Solution(StrSplitSolution):
    _year = 2024
    _day = 25

    separator = "\n\n"

    def calculate_column_height(self, lines):
        # calculate the height of the each column
        column_height = [-1] * len(lines[0])
        for line in lines:
            for i, char in enumerate(line):
                if char == "#":
                    column_height[i] += 1
        return column_height

    # @answer(1234)
    def part_1(self) -> int:
        ans = 0
        keys = set()
        locks = set()

        for part in self.input:
            lines = part.split("\n")
            heights = self.calculate_column_height(lines)
            if lines[0][0] == "#":
                locks.add(tuple(heights))
            else:
                keys.add(tuple(heights))

        for l in locks:
            for k in keys:
                if all(l[i] + k[i] <= 5 for i in range(len(l))):
                    ans += 1

        return ans

    # @answer(1234)
    def part_2(self) -> int:
        ans = 0
        return ans
