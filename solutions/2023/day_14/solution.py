# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/14

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 14


    @answer(105784)
    def part_1(self) -> int:
        grid = self.input
        grid = list(map("".join, zip(*grid)))

        grid = [ '#'.join(["".join(sorted(list(group), reverse=True)) for group in row.split('#')]) for row in grid]
        grid = list(map("".join, zip(*grid)))

        ans = 0

        for r in range(len(grid)):
            row = grid[r]
            count = row.count('O')
            ans += count * (len(grid) - r)
        return ans




        


    @answer(91286)
    def part_2(self) -> int:
        global grid1  # Declare grid1 as a global variable

        grid1 = tuple(self.input)

        def cycle():
            global grid1  # Use nonlocal to refer to the global variable
            for _ in range(4):
                grid1 = list(map("".join, zip(*grid1)))
                grid1 = tuple('#'.join(["".join(sorted(list(group), reverse=True)) for group in row.split('#')]) for row in grid1)
                grid1 = tuple(row[::-1] for row in grid1)

        seen = {grid1}
        array = [grid1]

        iter = 0

        while True:
            iter += 1
            cycle()
            if grid1 in seen:
                break
            seen.add(grid1)
            array.append(grid1)

        first = array.index(grid1)
        grid1 = array[(1000000000 - first) % (iter - first) + first]

        ans = 0
        for r in range(len(grid1)):
            row = grid1[r]
            count = row.count('O')
            ans += count * (len(grid1) - r)
        return ans
        # @answer((1234, 4567))
        # def solve(self) -> tuple[int, int]:
        #     pass
