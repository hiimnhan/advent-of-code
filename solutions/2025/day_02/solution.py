# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/2

from ...base import StrSplitSolution, answer
import sys
import re
from collections.abc import Iterator

sys.setrecursionlimit(10000)


def iter_ranges(raw_ranges: list[str]) -> Iterator[int]:
    for raw_range in raw_ranges:
        start, end = map(int, raw_range.split("-"))
        yield from range(start, end + 1)


class Solution(StrSplitSolution):
    _year = 2025
    _day = 2
    separator = ","

    # @answer(1234)
    def part_1(self) -> int:
        regex = re.compile(r"^(.+)\1$")
        return sum(n for n in iter_ranges(self.input) if regex.match(str(n)))

    # @answer(1234)
    def part_2(self) -> int:
        regex = re.compile(r"^(.+)\1+$")
        return sum(n for n in iter_ranges(self.input) if regex.match(str(n)))
