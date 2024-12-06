# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/6

from ...base import StrSplitSolution, answer
import sys

sys.setrecursionlimit(10000)


class Solution(StrSplitSolution):
    _year = 2024
    _day = 6

    mp = {
        "^": ">",
        ">": "v",
        "v": "<",
        "<": "^",
    }

    # traverse the grid when hit # turn right, count the step
    def traverse(self, grid, r, c, visited):
        def out_of_bound(r, c):
            return r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0])

        def print_grid():
            for row in grid:
                print("".join(row))
            print()

        print(r, c, grid[r][c])
        match grid[r][c]:
            case "^":
                visited.add((r, c))
                if out_of_bound(r - 1, c):
                    print_grid()
                    return len(visited)
                if grid[r - 1][c] != "#":
                    grid[r - 1][c] = grid[r][c]
                    self.traverse(grid, r - 1, c, visited)
                else:
                    grid[r][c] = self.mp[grid[r][c]]
                    self.traverse(grid, r, c, visited)
            case ">":
                visited.add((r, c))
                if out_of_bound(r, c + 1):
                    print_grid()
                    return len(visited)
                if grid[r][c + 1] != "#":
                    grid[r][c + 1] = grid[r][c]
                    self.traverse(grid, r, c + 1, visited)
                else:
                    grid[r][c] = self.mp[grid[r][c]]
                    self.traverse(grid, r, c, visited)
            case "v":
                visited.add((r, c))
                if out_of_bound(r + 1, c):
                    print_grid()
                    return len(visited)
                if grid[r + 1][c] != "#":
                    grid[r + 1][c] = grid[r][c]
                    self.traverse(grid, r + 1, c, visited)
                else:
                    grid[r][c] = self.mp[grid[r][c]]
                    self.traverse(grid, r, c, visited)
            case "<":
                visited.add((r, c))
                if out_of_bound(r, c - 1):
                    print_grid()
                    return len(visited)
                if grid[r][c - 1] != "#":
                    grid[r][c - 1] = grid[r][c]
                    self.traverse(grid, r, c - 1, visited)
                else:
                    grid[r][c] = self.mp[grid[r][c]]
                    self.traverse(grid, r, c, visited)
        return len(visited)

    @answer(4696)
    def part_1(self) -> int:
        grid = [
            [self.input[i][j] for j in range(len(self.input[0]))]
            for i in range(len(self.input))
        ]
        R = len(grid)
        C = len(grid[0])
        print(grid)

        visited = set()

        for row in range(R):
            for col in range(C):
                if grid[row][col] == "^":
                    return self.traverse(grid, row, col, visited)
        return 0

    # @answer(1234)
    def part_2(self) -> int:
        pass
