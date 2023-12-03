# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/2

import re
from collections import defaultdict
from functools import reduce
from operator import mul

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 2

    @answer(2265)
    def part_1(self) -> int:
        total = 0
        for idx, game in enumerate(self.input):
            _, mables = game.split(': ')

            if all(
                int(count) <= {"red": 12, "green": 13, "blue": 14}[color]
                for count, color in re.findall(r"(\d+) (\w+)", mables)
            ):
                total += idx + 1
        return total

    @answer(64097)
    def part_2(self) -> int:
        total = 0
        for game in self.input:
            _, mables = game.split(': ')
            mins = defaultdict(int)

            for count, color in re.findall(r"(\d+) (\w+)", mables):
                mins[color] = max(mins[color], int(count))
            total += reduce(mul, mins.values())
        return total

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
