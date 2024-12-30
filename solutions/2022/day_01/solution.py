# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2022/day/1

from ...base import StrSplitSolution, answer
import sys
import heapq

sys.setrecursionlimit(10000)


class Solution(StrSplitSolution):
    _year = 2022
    _day = 1

    separator = "\n\n"

    @answer(64929)
    def part_1(self) -> int:
        ans = 0

        for line in self.input:
            sm = sum(map(int, line.split("\n")))
            ans = max(ans, sm)
        return ans

    @answer(193697)
    def part_2(self) -> int:
        ans = 0
        heap = []

        for line in self.input:
            sm = sum(map(int, line.split("\n")))
            heapq.heappush(heap, -sm)

        i = 0
        while i < 3:
            ans += -heapq.heappop(heap)
            i += 1
        return ans
