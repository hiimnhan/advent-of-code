# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/1

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 1

    first_col = []
    second_col = []

    @answer(2815556)
    def part_1(self) -> int:
        for line in self.input:
            first, second = line.split("   ")
            self.first_col.append(int(first))
            self.second_col.append(int(second))
        self.first_col.sort()
        self.second_col.sort()

        ans = 0

        for f, se in zip(self.first_col, self.second_col):
            ans += abs(f - se)
        return ans

    @answer(23927637)
    def part_2(self) -> int:
        ans = 0
        for i in range(len(self.first_col)):
            ans += self.first_col[i] * self.second_col.count(self.first_col[i])

        return ans

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
