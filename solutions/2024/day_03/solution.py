# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/3

from ...base import TextSolution, answer
import sys
import re

sys.setrecursionlimit(10000)


class Solution(TextSolution):
    _year = 2024
    _day = 3

    def find_do_in_substring(self, s) -> bool:
        # find do() in the string
        return "do()" in s

    def find_dont_in_substring(self, s) -> bool:
        # find don't() in the string
        return "don't()" in s

    def extract_substring(self, s):
        pattern = r"mul\(\s*([-+]?\d*\.?\d+)\s*,\s*([-+]?\d*\.?\d+)\s*\)"
        matches = []

        for m in re.finditer(pattern, s):
            start, end = m.span()
            matches.append((m.groups(), start, end))
        return matches

    @answer(167090022)
    def part_1(self) -> int:
        ans = 0
        for group, _, _ in self.extract_substring(self.input):
            first, second = group
            ans += int(first) * int(second)
        return ans

    @answer(89823704)
    def part_2(self) -> int:
        ans = 0
        track = 0
        for group, start, end in self.extract_substring(self.input):
            if self.find_do_in_substring(self.input[track:start]):
                first, second = group
                ans += int(first) * int(second)
                track = end
                continue
            if self.find_dont_in_substring(self.input[track:start]):
                continue
            else:
                first, second = group
                ans += int(first) * int(second)
                track = end

        return ans

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
