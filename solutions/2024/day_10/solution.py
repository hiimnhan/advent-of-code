# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/10

from collections import deque
from solutions.utils.grid import is_out_of_bounds, make_grid
from ...base import StrSplitSolution, answer
import sys

sys.setrecursionlimit(10000)


class Solution(StrSplitSolution):
    _year = 2024
    _day = 10

    def traverse(self, grid, x, y) -> tuple[int, int]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # BFS
        queue = deque([(x, y)])
        visited = set()

        reachable = []

        while queue:
            r, c = queue.popleft()
            val = grid[r][c]

            for dx, dy in directions:
                nx, ny = r + dx, c + dy

                if not is_out_of_bounds(grid, nx, ny):
                    next_val = grid[nx][ny]
                    if next_val == val + 1 and (nx, ny) not in visited:
                        queue.append((nx, ny))
                        if next_val == 9:
                            reachable.append((nx, ny))

        return len(set(reachable)), len(reachable)

    @answer(638)
    def part_1(self) -> int:
        ans = 0
        grid = make_grid(self.input, to_int=True)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    reachable, _ = self.traverse(grid, r, c)
                    ans += reachable
        return ans

    @answer(1289)
    def part_2(self) -> int:
        ans = 0
        grid = make_grid(self.input, to_int=True)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    _, reachable = self.traverse(grid, r, c)
                    ans += reachable
        return ans
