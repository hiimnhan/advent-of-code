# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/11

from copy import deepcopy
from ...base import IntSplitSolution, answer
import sys

sys.setrecursionlimit(10000)


class Solution(IntSplitSolution):
    _year = 2024
    _day = 11

    separator = " "

    def blink(self, input):
        new_line = []

        for n in input:
            if n == 0:
                new_line.append(1)
                continue
            elif len(str(n)) % 2 == 0:
                left, right = self.split_number_evenly(n)
                new_line.append(left)
                new_line.append(right)
                continue
            else:
                new_line.append(n * 2024)
        return new_line

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
        input = deepcopy(self.input)
        for _ in range(25):
            input = self.blink(input)
            print(input)
        return len(input)

    # @answer(1234)
    def part_2(self) -> int:
        ans = 0
        return ans
