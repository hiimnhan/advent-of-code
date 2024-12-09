# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/9

from ...base import IntSolution, answer
import sys

sys.setrecursionlimit(10000)
sys.set_int_max_str_digits(0)


class Solution(IntSolution):
    _year = 2024
    _day = 9

    separator = None

    def generate_blocks(self, input):
        blocks = []
        free_spots = []
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
                    idx = len(blocks)
                    free_spots.append(idx)
                    blocks.append(None)
            is_prev_a_file = not is_prev_a_file
        return blocks, free_spots, file_starts

    # @answer(1234)
    def part_1(self) -> int:
        ans = 0
        blocks, free_spots, _ = self.generate_blocks(str(self.input))
        for pos in free_spots:
            if pos > len(blocks):
                break
            val = blocks.pop()
            blocks[pos] = val
            while blocks[-1] is None:
                blocks.pop()

        for pos, v in enumerate(blocks):
            ans += pos * v
        return ans

    # @answer(1234)
    def part_2(self) -> int:
        ans = 0
        blocks, _, file_starts = self.generate_blocks(str(self.input))

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
