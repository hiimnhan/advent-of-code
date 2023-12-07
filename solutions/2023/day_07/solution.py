# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/7

from collections import Counter, defaultdict

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 7

    RANK_CARD = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': 11,
        'T': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2,
        '1': 1
    }


    def rank(self, hand):
        counts = [hand.count(card) for card in hand]
        if 5 in counts:
            return 6
        if 4 in counts:
            return 5
        if 3 in counts:
            if 2 in counts:
                return 4
            return 3
        if counts.count(2) == 4:
            return 2
        if 2 in counts:
            return 1
        return 0

    def strength(self, hand):
        return (self.rank(hand), [self.RANK_CARD.get(card, card) for card in hand])
    # @answer(1234)
    def part_1(self) -> int:
        hands = []
        for index, line in enumerate(self.input):
            [cards, bid] = line.split(" ")
            hands.append((cards, int(bid)))
        hands.sort(key=lambda play: self.strength(play[0]))

        total = 0
        for rank, (hand, bid) in enumerate(hands, 1):
            total += rank * bid

        return total



        






        return -1

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
