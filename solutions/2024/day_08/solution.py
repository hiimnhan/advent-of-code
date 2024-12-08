# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/8

from itertools import combinations

from solutions.utils.util import make_grid, print_grid

from ...base import StrSplitSolution, answer
from collections import defaultdict
import sys

sys.setrecursionlimit(10000)


class Solution(StrSplitSolution):
    _year = 2024
    _day = 8

    def is_in_bounds(self, grid, coord):
        x, y = coord
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])

    def linear_equation(self, coord1, coord2):
        x1, y1 = coord1
        x2, y2 = coord2
        m = (y2 - y1) / (x2 - x1)
        b = y1 - m * x1
        return m, b

    def mahattan_distance(self, coord1, coord2):
        x1, y1 = coord1
        x2, y2 = coord2
        return abs(x2 - x1) + abs(y2 - y1)

    def is_on_line(self, m, b, coord):
        x, y = coord
        return y == m * x + b

    def find_coords_on_line_with_distance(self, grid, coord1, coord2):
        m, b = self.linear_equation(coord1, coord2)
        distance = self.mahattan_distance(coord1, coord2)

        coords = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if self.is_on_line(m, b, (r, c)):
                    if (r, c) == coord1 or (r, c) == coord2:
                        continue
                    if (
                        self.mahattan_distance(coord1, (r, c)) == distance
                        or self.mahattan_distance(coord2, (r, c)) == distance
                    ):
                        coords.append((r, c))
        return coords

    # @answer(1234)
    def part_1(self) -> int:
        map = defaultdict(set)
        existed = set()
        grid = make_grid(self.input)
        R, C = len(grid), len(grid[0])
        for r in range(R):
            for c in range(C):
                if grid[r][c] == ".":
                    continue
                map[grid[r][c]].add((r, c))
        print(map)
        for anten in map:
            coords = list(map[anten])
            combs = list(combinations(coords, 2))
            for comb in combs:
                coords_on_line = self.find_coords_on_line_with_distance(grid, *comb)
                print(f"coords_on_line: {coords_on_line}, comb: {comb}")
                for coord in coords_on_line:
                    if self.is_in_bounds(grid, coord):
                        print(coord)
                        existed.add(coord)
                        if grid[coord[0]][coord[1]] == ".":
                            grid[coord[0]][coord[1]] = "#"
        print_grid(grid)
        return len(existed)

    # @answer(1234)
    def part_2(self) -> int:
        pass
