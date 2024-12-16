# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/14

import sys

from ...base import StrSplitSolution

sys.setrecursionlimit(10000)


class Solution(StrSplitSolution):
    _year = 2024
    _day = 14

    WIDTH = 101
    HEIGHT = 103

    def parse(self, input):
        data = []
        for line in input:
            p, v = line.split(" ")
            px, py = map(int, p.split("=")[1].split(","))
            vx, vy = map(int, v.split("=")[1].split(","))
            data.append((px, py, vx, vy))
        return data

    def check_is_center(self, r, c):
        hw = self.WIDTH // 2
        hh = self.HEIGHT // 2

        return r == hh and c == hw

    def process(self, px, py, vx, vy, time):
        dx = vx * time
        dy = vy * time

        return ((px + dx) % self.WIDTH, (py + dy) % self.HEIGHT)

    # @answer(1234)
    def part_1(self) -> int:
        ans = 1
        data = self.parse(self.input)
        q1, q2, q3, q4 = 0, 0, 0, 0

        for d in data:
            px, py, vx, vy = d
            x, y = self.process(px, py, vx, vy, 100)
            print(x, y)
            if x < self.WIDTH // 2 and y < self.HEIGHT // 2:
                q1 += 1
            elif x < self.WIDTH // 2 and y > self.HEIGHT // 2:
                q2 += 1
            elif x > self.WIDTH // 2 and y < self.HEIGHT // 2:
                q3 += 1
            elif x > self.WIDTH // 2 and y > self.HEIGHT // 2:
                q4 += 1

        print(q1, q2, q3, q4)
        return q1 * q2 * q3 * q4

    # @answer(1234)
    def part_2(self) -> int:
        ans = 0
        return ans
