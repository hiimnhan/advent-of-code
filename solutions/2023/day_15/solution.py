# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/15

from ...base import TextSolution, answer


class Solution(TextSolution):
    _year = 2023
    _day = 15

    def hash(self, string):
        value = 0
        for c in string:
            value += ord(c)
            value *= 17
            value %= 256
        return value


    # @answer(1234)
    def part_1(self) -> int:
        parts = self.input.split(',')
        ans = 0
        for part in parts:
            ans += self.hash(part)

        return ans

    # @answer(1234)
    def part_2(self) -> int:
        def split(s):
            if "=" in s:
                op = "="
                label, num = s.split('=')
                num = int(num)
            elif '-' in s:
                op = '-'
                label = s.split('-')[0]
                num = None
            return op, label, num
        
        def handle(s, boxes):
            op, label, num = split(s)
            box_id = self.hash(s)

            if op == '-':
                try:
                    boxes[box_id].pop(label)
                except KeyError:
                    pass
            else:
                boxes[box_id][label] = num

        boxes = [{} for _ in range(256)]
        for s in self.input.split(','):
            handle(s, boxes)

        print(boxes)

        total = 0
        for box_id, box in enumerate(boxes, 1):
            for slot, num in enumerate(box.values(), 1):
                total += box_id * slot * num
        return total


    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
