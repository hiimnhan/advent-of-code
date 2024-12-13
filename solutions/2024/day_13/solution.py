# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/13

from ...base import StrSplitSolution, answer
import sys

sys.setrecursionlimit(10000)


class Solution(StrSplitSolution):
    _year = 2024
    _day = 13

    def parse(self, lines, rate=0):
        N = len(lines)
        machines = []
        for i in range(0, N, 4):
            a_x, a_y = map(
                int,
                lines[i]
                .split(":")[1]
                .strip()
                .replace("X+", "")
                .replace("Y+", "")
                .split(","),
            )
            b_x, b_y = map(
                int,
                lines[i + 1]
                .split(":")[1]
                .strip()
                .replace("X+", "")
                .replace("Y+", "")
                .split(","),
            )
            p_x, p_y = map(
                int,
                lines[i + 2]
                .split(":")[1]
                .strip()
                .replace("X=", "")
                .replace("Y=", "")
                .split(","),
            )
            p_x = 1 * rate + p_x
            p_y = 1 * rate + p_y
            machines.append((a_x, a_y, b_x, b_y, p_x, p_y))
        return machines

    def process(self, machines, max_presses) -> int:
        total = 0

        for i, machines in enumerate(machines):
            a_x, a_y, b_x, b_y, p_x, p_y = machines
            min_cost = float("inf")
            for x in range(0, max_presses + 1):
                for y in range(0, max_presses + 1):
                    result_x = a_x * x + b_x * y
                    result_y = a_y * x + b_y * y

                    if result_x == p_x and result_y == p_y:
                        cost = 3 * x + y
                        min_cost = min(min_cost, cost)
            if min_cost != float("inf"):
                total += min_cost
        return int(total)

    # @answer(1234)
    def part_1(self) -> int:
        ans = 0
        machines = self.parse(self.input)
        ans += self.process(machines, 100)
        return ans

    # @answer(1234)
    def part_2(self) -> int:
        RATE = 10**13
        ans = 0
        machines = self.parse(self.input, RATE)
        return ans
