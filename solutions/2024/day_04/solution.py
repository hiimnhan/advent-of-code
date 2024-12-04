# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/4

from ...base import StrSplitSolution, answer
import sys

sys.setrecursionlimit(10000)


class Solution(StrSplitSolution):
    _year = 2024
    _day = 4

    mat = []
    ROW = 0
    COL = 0

    def matrix(self):
        self.mat = [list(row) for row in self.input]
        self.ROW = len(self.mat)
        self.COL = len(self.mat[0])

    def traverse_p1(self, word):
        def is_valid(row, col):
            return 0 <= row < self.ROW and 0 <= col < self.COL

        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (1, 1),
            (-1, -1),
            (1, -1),
            (-1, 1),
        ]

        count = 0

        for row in range(self.ROW):
            for col in range(self.COL):
                for dr, dc in directions:
                    match = True
                    for i in range(len(word)):
                        r, c = row + i * dr, col + i * dc
                        if not is_valid(r, c) or self.mat[r][c] != word[i]:
                            match = False
                            break
                    if match:
                        count += 1
        return count

    def traverse_p2(self):
        count = 0

        for row in range(1, self.ROW - 1):
            for col in range(1, self.COL - 1):
                if self.mat[row][col] == "A":
                    cross1 = self.mat[row - 1][col - 1] + self.mat[row + 1][col + 1]
                    cross2 = self.mat[row - 1][col + 1] + self.mat[row + 1][col - 1]
                    if (cross1 == "MS" or cross1 == "SM") and (
                        cross2 == "MS" or cross2 == "SM"
                    ):
                        count += 1
        return count

    @answer(2567)
    def part_1(self) -> int:
        self.matrix()
        return self.traverse_p1("XMAS")

    @answer(2029)
    def part_2(self) -> int:
        return self.traverse_p2()
