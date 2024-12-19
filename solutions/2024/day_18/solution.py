# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/18

from solutions.utils.grid import (
    dijkstra,
)
from ...base import StrSplitSolution, answer
import sys
from math import inf

sys.setrecursionlimit(10000)


class Solution(StrSplitSolution):
    _year = 2024
    _day = 18

    @answer(382)
    def part_1(self) -> int:
        W = H = int(self.input[0])
        assert W == H
        assert W != -1

        stop = int(self.input[1])
        assert stop != 0

        corrupted = set()

        for line in self.input[2 : stop + 2]:
            r, c = map(int, line.split(","))
            corrupted.add((c, r))

        return dijkstra(W, H, (0, 0), (W, H), corrupted)

    @answer((6, 36))
    def part_2(self) -> tuple[int, int]:
        W = H = int(self.input[0])
        assert W == H
        assert W != -1

        stop = int(self.input[1])
        assert stop != 0

        corrupted = set()

        for line in self.input[2 : stop + 2]:
            r, c = map(int, line.split(","))
            corrupted.add((c, r))

        for line in self.input[stop + 2 :]:
            r, c = map(int, line.split(","))
            corrupted.add((c, r))
            if dijkstra(W, H, (0, 0), (W, H), corrupted) == inf:
                return (r, c)

        return 0, 0
