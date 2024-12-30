# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2022/day/2

from ...base import StrSplitSolution, answer
import sys

sys.setrecursionlimit(10000)


class Solution(StrSplitSolution):
    _year = 2022
    _day = 2

    @answer(13526)
    def part_1(self) -> int:
        ans = 0
        counter_parts = {
            "A": "B",
            "B": "C",
            "C": "A",
        }

        mp = {
            "X": "A",
            "Y": "B",
            "Z": "C",
        }

        points = {
            "X": 1,
            "Y": 2,
            "Z": 3,
        }

        for line in self.input:
            a, b = line.split(" ")
            c = mp[b]
            if a == c:
                ans += points[b] + 3
                continue
            if counter_parts[a] == c:
                ans += points[b] + 6
                continue
            ans += points[b]
        return ans

    @answer(14204)
    def part_2(self) -> int:
        ans = 0
        counter_parts = {
            "A": "B",
            "B": "C",
            "C": "A",
        }

        lose = {
            "A": "C",
            "B": "A",
            "C": "B",
        }

        points = {
            "A": 1,
            "B": 2,
            "C": 3,
        }

        for line in self.input:
            a, b = line.split(" ")
            match b:
                case "X":
                    ans += points[lose[a]]
                    continue
                case "Y":
                    ans += points[a] + 3
                    continue
                case "Z":
                    ans += points[counter_parts[a]] + 6
                    continue
        return ans
