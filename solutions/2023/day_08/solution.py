# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/8

from itertools import cycle

import numpy as np

from ...base import TextSolution, answer


class Solution(TextSolution):
    _year = 2023
    _day = 8

    G = {}

    def parse(self, input):
        instruction, map = input.split('\n\n')
        for m in map.split('\n'):
            source, dest = m.split(' = ')
            self.G[source] = [d.replace('(', '').replace(')', '') for d in dest.split(', ')]
        return (instruction, map)



    @answer(24253)
    def part_1(self) -> int:
        step = 0
        instruction, map = self.parse(self.input)
        
        start = 'AAA'
        for idx, i in enumerate(cycle(instruction), 1):
            if i == 'L':
                start = self.G[start][0]
            else:
                start = self.G[start][1]
            step += 1
            if start == 'ZZZ':
                return step
        return 0





    @answer(12357789728873)
    # credit: https://github.com/wleftwich/aoc/blob/main/2023/08-haunted-wasteland.ipynb
    def part_2(self) -> int:
        instruction, map = self.parse(self.input)

        def one_path_steps_to_starz(k, steps, nwmap):
            for i, step in enumerate(cycle(steps), 1):
                k = nwmap[k][0 if step == 'L' else 1]
                if k.endswith('Z'):
                    break
            return i, k
        
        def two_cycle(k, steps, nwmap):
            i, k = one_path_steps_to_starz(k, steps, nwmap)
            j, k = one_path_steps_to_starz(k, steps, nwmap)
            return i, j, k
        
        ns = [one_path_steps_to_starz(k, instruction, self.G)[0] for k in self.G.keys() if k.endswith('A')]
        return np.lcm.reduce(ns)






    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
