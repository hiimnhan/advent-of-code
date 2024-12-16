# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/13

import sys

from ...base import StrSplitSolution

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

    def process(self, machines) -> int:
        total = 0

        # solve linear equations
        # a*ax + b*bx = px
        # a*ay + b*by = py

        for machine in machines:
            ax, ay, bx, by, px, py = machine
            if by == 0 or ax == ay * bx / by:
                return total
            a = (px - py * bx / by) / (ax - ay * bx / by)
            b = (py - a * ay) / by
            ra, rb = round(a), round(b)

            if (
                (ra * ax + rb * bx == px)
                and (ra * ay + rb * by == py)
                and ra >= 0
                and rb >= 0
            ):
                total += 3 * a + b

        return int(total)

    # @answer(1234)
    def part_1(self) -> int:
        ans = 0
        machines = self.parse(self.input)
        ans += self.process(machines)
        return ans

    # @answer(1234)
    def part_2(self) -> int:
        RATE = 10**13
        ans = 0
        machines = self.parse(self.input, RATE)
        ans += self.process(machines)
        return ans
