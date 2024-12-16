# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/16

import heapq
import sys
from math import inf

from solutions.utils.grid import (
    DIRECTIONS,
    is_out_of_bounds,
    make_grid,
    next_directions_by_degree,
)

from ...base import StrSplitSolution

sys.setrecursionlimit(10000)


class Solution(StrSplitSolution):
    _year = 2024
    _day = 16

    # @answer(1234)
    def part_1(self) -> int:
        grid = make_grid(self.input)
        R, C = len(grid), len(grid[0])
        visited = set()
        heap = []
        best = inf
        costs = {}
        sr, sc, er, ec = -1, -1, -1, -1
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "S":
                    sr, sc = r, c
                if grid[r][c] == "E":
                    er, ec = r, c
        assert sr != -1 and sc != -1 and er != -1 and ec != -1
        heapq.heappush(heap, (0, sr, sc, 1))
        while heap:
            cost, r, c, d = heapq.heappop(heap)
            if (r, c, d) not in costs:
                costs[(r, c, d)] = cost
            if r == er and c == ec:
                best = min(best, cost)
            if (r, c, d) in visited:
                continue
            visited.add((r, c, d))
            dr, dc = DIRECTIONS[d]
            nr, nc = r + dr, c + dc
            if not is_out_of_bounds(grid, nr, nc) and grid[nr][nc] != "#":
                heapq.heappush(heap, (cost + 1, nr, nc, d))
            ndl, ndr = next_directions_by_degree(d)
            heapq.heappush(heap, (cost + 1000, r, c, ndl))
            heapq.heappush(heap, (cost + 1000, r, c, ndr))

        assert best != inf
        return int(best)

    # @answer(1234)
    def part_2(self) -> int:
        ans = 0
        return ans
