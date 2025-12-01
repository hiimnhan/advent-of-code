# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/1

from ...base import StrSplitSolution, answer
import sys

sys.setrecursionlimit(10000)


class Solution(StrSplitSolution):
    _year = 2025
    _day = 1

    @answer(1165)
    def part_1(self) -> int:
        ans = 0
        current = 50
        for line in self.input:
            direction, num = line[0], int(line[1:])
            if direction == "L":
                current -= num
            elif direction == "R":
                current += num
            if current == 0 or current % 100 == 0:
                ans += 1
        return ans

    @answer(6496)
    def part_2(self) -> int:
        ans = 0
        current = 50
        prev = 50
        for line in self.input:
            direction, num = line[0], int(line[1:])
            prev = current
            if direction == "L":
                current = prev - num
                ans += current // 100 - prev // 100
            elif direction == "R":
                current = prev + num
                ans += (prev - 1) // 100 - (current - 1) // 100
        return ans
