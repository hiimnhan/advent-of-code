# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/15

import sys

from solutions.utils.grid import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    make_grid,
    next_coord,
)

from ...base import StrSplitSolution

sys.setrecursionlimit(10000)


class Solution(StrSplitSolution):
    _year = 2024
    _day = 15

    separator = "\n\n"

    directions = {
        ">": RIGHT,
        "<": LEFT,
        "^": UP,
        "v": DOWN,
    }

    def push(self, grid, r, c, step, walls, boxes):
        d = self.directions[step]
        nxt = next_coord(r, c, *d)
        if nxt in walls:
            return False
        if nxt in boxes:
            if not self.push(grid, *nxt, step, walls, boxes):
                return False
        boxes.remove((r, c))
        boxes.add(nxt)
        return True

    # @answer(1234)
    def part_1(self) -> int:
        ans = 0
        grid = self.input[0].split("\n")
        steps = self.input[1]
        grid = make_grid(grid)
        R, C = len(grid), len(grid[0])
        walls = set()
        boxes = set()

        for r in range(R):
            for c in range(C):
                if grid[r][c] == "@":
                    robot = (r, c)
                elif grid[r][c] == "#":
                    walls.add((r, c))
                elif grid[r][c] == "O":
                    boxes.add((r, c))
        for step in steps:
            d = self.directions[step]
            nxt = next_coord(*robot, *d)
            if nxt in walls:
                continue
            if nxt in boxes:
                if not self.push(grid, nxt[0], nxt[1], step, walls, boxes):
                    continue
            assert nxt not in boxes
            robot = nxt

        for box in boxes:
            ans += box[0] * 100 + box[1]

        return ans

    # @answer(1234)
    def part_2(self) -> int:
        ans = 0
        return ans
