# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/11

import sys
from functools import cache

from ...base import IntSplitSolution

sys.setrecursionlimit(10000)


class Solution(IntSplitSolution):
    _year = 2024
    _day = 11

    separator = " "

    @cache
    def blink(self, num) -> tuple[int, ...]:
        if num == 0:
            return (1,)
        if len(str(num)) % 2 == 0:
            return tuple(self.split_number_evenly(num))
        else:
            return (num * 2024,)

    @cache
    def process(self, nums: tuple[int, ...], times=25) -> int:
        if times == 0:
            return len(nums)
        return sum(self.process(self.blink(num), times - 1) for num in nums)

    def split_number_evenly(self, number: int, parts=2) -> list[int]:
        num_str = str(number)
        num_digits = len(num_str)

        if num_digits % parts != 0:
            assert False

        part_len = num_digits // parts
        return [int(num_str[i : i + part_len]) for i in range(0, num_digits, part_len)]

    # @answer(1234)
    def part_1(self) -> int:
        ans = 0
        input = tuple(self.input)
        return self.process(input)

    # @answer(1234)
    def part_2(self) -> int:
        ans = 0
        input = tuple(self.input)
        return self.process(input, 75)
