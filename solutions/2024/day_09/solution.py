# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/9

import sys

from ...base import IntSolution, answer

sys.setrecursionlimit(10000)
sys.set_int_max_str_digits(0)


class Solution(IntSolution):
    _year = 2024
    _day = 9

    separator = None

    def generate_blocks(self, input):
        blocks = []
        file_starts = []
        is_prev_a_file = True
        i = 0
        for x in input:
            if is_prev_a_file:
                file_starts.append(len(blocks))
                for _ in range(int(x)):
                    blocks.append(i)
                i += 1
            else:
                for _ in range(int(x)):
                    blocks.append(None)
            is_prev_a_file = not is_prev_a_file
        return blocks, file_starts

    @answer(6334655979668)
    def part_1(self) -> int:
        ans = 0
        blocks, _ = self.generate_blocks(str(self.input))

        i, j = 0, len(blocks) - 1

        while i < j:
            if blocks[i] is not None:
                i += 1
                continue
            if blocks[j] is None:
                j -= 1
                continue
            blocks[i], blocks[j] = blocks[j], blocks[i]
            i += 1
            j -= 1

        for pos, v in enumerate(blocks):
            if v is not None:
                ans += pos * v
        return ans

    @answer(6349492251099)
    def part_2(self) -> int:
        ans = 0
        blocks, file_starts = self.generate_blocks(str(self.input))

        def find_place(length):
            for idx, v in enumerate(blocks):
                if v is None and idx + length <= len(blocks):
                    if all(blocks[idx + i] is None for i in range(length)):
                        return idx

        while file_starts:
            idx = file_starts.pop()
            id = blocks[idx]
            end = idx
            while end + 1 < len(blocks) and blocks[end + 1] == id:
                end += 1
            length = end - idx + 1

            place = find_place(length)
            if place is None:
                continue
            if place < idx:
                for i in range(length):
                    blocks[place + i] = id
                    blocks[idx + i] = None

        for i, n in enumerate(blocks):
            if n is not None:
                ans += n * i

        return ans
