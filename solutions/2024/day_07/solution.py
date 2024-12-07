# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/7

from ...base import StrSplitSolution, answer
from collections import defaultdict
import sys

sys.setrecursionlimit(10000)


class Solution(StrSplitSolution):
    _year = 2024
    _day = 7

    def is_valid(self, target, numbers, has_concat=False):
        def concat(a, b):
            return int(str(a) + str(b))

        dp = defaultdict(set)
        dp[0].add(numbers[0])

        for i in range(1, len(numbers)):
            current = numbers[i]
            new_dp = defaultdict(set)
            for value in dp[i - 1]:
                new_dp[i].add(value + current)
                new_dp[i].add(value * current)
                if has_concat:
                    new_dp[i].add(concat(value, current))
            dp[i] = new_dp[i]

        return target in dp[len(numbers) - 1]

    @answer(1298103531759)
    def part_1(self) -> int:
        ans = 0
        for line in self.input:
            target, numbers = line.split(": ")
            target = int(target)
            numbers = list(map(int, numbers.split(" ")))
            if self.is_valid(target, numbers):
                ans += target
        return ans

    @answer(140575048428831)
    def part_2(self) -> int:
        ans = 0
        for line in self.input:
            target, numbers = line.split(": ")
            target = int(target)
            numbers = list(map(int, numbers.split(" ")))
            if self.is_valid(target, numbers, has_concat=True):
                ans += target
        return ans
