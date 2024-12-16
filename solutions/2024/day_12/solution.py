# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/12

import sys

from solutions.utils.grid import connected_regions, make_grid

from ...base import StrSplitSolution

sys.setrecursionlimit(10000)


class Solution(StrSplitSolution):
    _year = 2024
    _day = 12

    # @answer(1234)
    def part_1(self) -> int:
        ans = 0
        grid = make_grid(self.input)
        components = connected_regions(grid)
        # print(components)
        for type, regions in components.items():
            for region in regions:
                ans += len(region[0]) * region[1]
        return ans

    # @answer(1234)
    def part_2(self) -> int:
        ans = 0
        grid = make_grid(self.input)
        components = connected_regions(grid)
        for type, regions in components.items():
            for region in regions:
                print(type, len(region[0]), region[2])
                ans += len(region[0]) * region[2]
        return ans
