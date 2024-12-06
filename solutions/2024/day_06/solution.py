# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/6

from ...base import StrSplitSolution, answer
import sys
import copy

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
    def print_grid(self, grid):
        for row in grid:
            print("".join(row))
        print()

    # traverse the grid when hit # turn right, count, loop the step
    def traverse(self, grid, r, c, visited, visited_cycle) -> tuple[set, bool]:
        def out_of_bound(r, c):
            return r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0])


        is_cycle = False
        if (r, c, grid[r][c]) in visited_cycle:
            is_cycle = True
            return visited, is_cycle
        visited_cycle.add((r, c, grid[r][c]))
        match grid[r][c]:
            case "^":
                visited.add((r, c))
                if out_of_bound(r - 1, c):
                    # print_grid()
                    return visited, is_cycle
                if grid[r - 1][c] != "#":
                    grid[r - 1][c] = grid[r][c]
                    is_cycle = self.traverse(grid, r - 1, c, visited, visited_cycle)[1]
                else:
                    grid[r][c] = self.mp[grid[r][c]]
                    is_cycle = self.traverse(grid, r, c, visited, visited_cycle)[1]
            case ">":
                visited.add((r, c))
                if out_of_bound(r, c + 1):
                    # print_grid()
                    return visited, is_cycle
                if grid[r][c + 1] != "#":
                    grid[r][c + 1] = grid[r][c]
                    is_cycle = self.traverse(grid, r, c + 1, visited, visited_cycle)[1]
                else:
                    grid[r][c] = self.mp[grid[r][c]]
                    is_cycle = self.traverse(grid, r, c, visited, visited_cycle)[1]
            case "v":
                visited.add((r, c))
                if out_of_bound(r + 1, c):
                    # print_grid()
                    return visited, is_cycle
                if grid[r + 1][c] != "#":
                    grid[r + 1][c] = grid[r][c]
                    is_cycle = self.traverse(grid, r + 1, c, visited, visited_cycle)[1]
                else:
                    grid[r][c] = self.mp[grid[r][c]]
                    is_cycle = self.traverse(grid, r, c, visited, visited_cycle)[1]
            case "<":
                visited.add((r, c))
                if out_of_bound(r, c - 1):
                    # print_grid()
                    return visited, is_cycle
                if grid[r][c - 1] != "#":
                    grid[r][c - 1] = grid[r][c]
                    is_cycle = self.traverse(grid, r, c - 1, visited, visited_cycle)[1]
                else:
                    grid[r][c] = self.mp[grid[r][c]]
                    is_cycle = self.traverse(grid, r, c, visited, visited_cycle)[1]
        if is_cycle:
            return visited, is_cycle
        return visited, is_cycle

    @answer(4696)
    def part_1(self) -> int:
        grid = [
            [self.input[i][j] for j in range(len(self.input[0]))]
            for i in range(len(self.input))
        ]
        R = len(grid)
        C = len(grid[0])


        for row in range(R):
            for col in range(C):
                if grid[row][col] == "^":
                    l, _ = self.traverse(grid, row, col, set(), set())
                    return len(l)
        return 0

    # @answer(1234)
    def part_2(self) -> int:
        grid = [
            [self.input[i][j] for j in range(len(self.input[0]))]
            for i in range(len(self.input))
        ]
        R = len(grid)
        C = len(grid[0])
        ans = set()

        for row in range(R):
            for col in range(C):
                if grid[row][col] == "^":
                    _grid = copy.deepcopy(grid)
                    visited, _ = self.traverse(_grid, row, col, set(), set())
                    for r, c in visited:
                        changed_grid = copy.deepcopy(grid) 
                        changed_grid[r][c] = "#"
                        _, is_cycle = self.traverse(changed_grid, row, col, set(), set())
                        if is_cycle:
                            ans.add((r, c)) 

        return len(ans)
