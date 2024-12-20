# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/20

from collections import defaultdict
from ...base import StrSplitSolution, answer
from solutions.utils.grid import (
    DIRECTIONS,
    dijkstra,
    dijkstra_and_path,
    find_turning_points,
    is_out_of_bounds,
    make_grid,
    next_coord,
    next_directions_by_degree,
    print_grid,
)
import sys

sys.setrecursionlimit(10000)


class Solution(StrSplitSolution):
    _year = 2024
    _day = 20

    # @answer(1234)
    def part_1(self) -> int:
        ans = 0
        grid = make_grid(self.input)
        # print_grid(grid)
        R, C = len(grid), len(grid[0])
        sr, sc, er, ec = -1, -1, -1, -1
        obstacles = set()
        roads = set()

        for r in range(R):
            for c in range(C):
                if grid[r][c] == "S":
                    sr, sc = r, c
                if grid[r][c] == "E":
                    er, ec = r, c
                if grid[r][c] == "#":
                    obstacles.add((r, c))
                if grid[r][c] == ".":
                    roads.add((r, c))
        assert sr != -1 and sc != -1 and er != -1 and ec != -1
        base_len, points = dijkstra_and_path(R, C, (sr, sc), (er, ec), obstacles)
        tps = find_turning_points(points)
        print(tps)
        dict = defaultdict(int)
        start = set()
        for tp in tps:
            for i, d in enumerate(DIRECTIONS):
                nxt = next_coord(*tp, *d)
                if is_out_of_bounds(grid, *nxt) or nxt not in obstacles or nxt in start:
                    continue
                start.add(nxt)
                for j, dd in enumerate(DIRECTIONS):
                    # can not go back
                    if j == next_directions_by_degree(i, deg=180)[0]:
                        continue
                    nxt2 = next_coord(*nxt, *dd)
                    if is_out_of_bounds(grid, *nxt2):
                        continue
                    #  next next can not be a wall
                    nxxt = next_coord(*nxt2, *dd)
                    if is_out_of_bounds(grid, *nxxt) or nxxt in obstacles:
                        continue
                    # assert not is_out_of_bounds(grid, *nxt2)
                    cloned_obstacles = obstacles.copy()
                    cloned_obstacles.remove(nxt)
                    if nxt2 in cloned_obstacles:
                        cloned_obstacles.remove(nxt2)
                    l = dijkstra(R, C, (sr, sc), (er, ec), cloned_obstacles)
                    dis = base_len - l
                    if dis + 1 > 0:
                        print(f"cheat: {(nxt, nxt2)} - {dis + 1}")
                        dict[dis + 1] += 1
                        ans += 1
        print(dict)
        return ans

    # @answer(1234)
    def part_2(self) -> int:
        ans = 0
        return ans
