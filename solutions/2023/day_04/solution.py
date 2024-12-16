# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/4


import numpy as np

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 4

    def get_win_nums_and_nums_have(self, line):
        win = []
        have = []
        _, piles = line.split(': ')
        pile1, pile2 = piles.split(' | ')
        win = [num for num in pile1.strip().split(' ') if num.isdigit()]
        have= [num for num in pile2.strip().split(' ') if num.isdigit()]
        return win, have

    @answer(22488)
    def part_1(self) -> int:
        ans = 0
        for line in self.input:
            win, have = self.get_win_nums_and_nums_have(line)
            count = 0
            for w in win:
                if w in have:
                    count += 1
            ans += pow(2, count - 1) if count > 0 else 0
        return ans




    @answer(7013204)
    def part_2(self) -> int:
        cardcount = np.ones(len(self.input), dtype=int)
        for i, line in enumerate(self.input):
            win, have = self.get_win_nums_and_nums_have(line)
            count = 0
            for w in win:
                if w in have:
                    count += 1
            start, stop = i + 1, i + 1 + count
            cardcount[start:stop] += cardcount[i]
        print(cardcount)
        return cardcount.sum()

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
