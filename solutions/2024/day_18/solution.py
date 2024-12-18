# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/18

from solutions.utils.grid import (
    bfs,
)
from ...base import StrSplitSolution
import sys

sys.setrecursionlimit(10000)


class Solution(StrSplitSolution):
    _year = 2024
    _day = 18

    # @answer(1234)
    def part_1(self) -> int:
        ans = 0
        W = H = int(self.input[0])
        assert W == H
        assert W != -1

        stop = int(self.input[1])
        assert stop != 0

        corrupted = set()

        for line in self.input[2 : stop + 2]:
            r, c = map(int, line.split(","))
            corrupted.add((c, r))

        return bfs(W, H, (0, 0), (W, H), corrupted)


    # @answer(1234)
    def part_2(self) -> int:
        ans = 0
        return ans
