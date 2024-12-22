# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/22

from itertools import product
from ...base import StrSplitSolution, answer
import sys

sys.setrecursionlimit(10000)


class Solution(StrSplitSolution):
    _year = 2024
    _day = 22

    def process(self, secret):
        MOD = 2**24

        secret ^= (secret * 64) % MOD
        secret %= MOD

        secret ^= (secret // 32) % MOD
        secret %= MOD

        secret ^= (secret * 2048) % MOD
        secret %= MOD

        return secret

    @answer(16999668565)
    def part_1(self) -> int:
        ans = 0
        steps = 2000

        for x in self.input:
            x = int(x)
            for _ in range(steps):
                x = self.process(x)
            ans += x
        return ans

    @answer(1898)
    def part_2(self) -> int:
        steps = 2000
        seq_to_total = {}

        for line in self.input:
            x = int(line)
            buyer = [x % 10]
            for _ in range(steps):
                x = self.process(x)
                buyer.append(x % 10)
            seen = set()
            for i in range(len(buyer) - 4):
                a, b, c, d, e = buyer[i : i + 5]
                seq = (b - a, c - b, d - c, e - d)
                if seq in seen:
                    continue
                seen.add(seq)
                if seq not in seq_to_total:
                    seq_to_total[seq] = 0
                seq_to_total[seq] += e

        return max(seq_to_total.values())
