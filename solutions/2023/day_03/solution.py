# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/3

import math
import re
from collections import defaultdict

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 3

    def iter_poss_partnums(self, data):
        for r, line in enumerate(data):
            for m in re.finditer(r"\d+", line):
                yield int(m.group()), [(r, c) for c in range(m.start(), m.end())]

    def neighbor(self, xy):
        x, y = xy
        return [
            (x + 1, y),
            (x + 1, y + 1),
            (x, y + 1),
            (x - 1, y + 1),
            (x - 1, y),
            (x, y - 1),
            (x - 1, y - 1),
            (x + 1, y - 1)
        ]


    @answer(535078)
    def part_1(self) -> int:
        def symbol_coord():
            coords = set()
            for r, line in enumerate(self.input):
                for m in re.finditer(r"[^\d\.]", line):
                    coords.add((r, m.start()))
            return coords
        
        

        
        def foundone(coordlist, symset):
            for rc in coordlist:
                for nabe in self.neighbor(rc):
                    if nabe in symset:
                        return True
            return False
        
        total = 0
        symset = symbol_coord()
        for partnum, coords in self.iter_poss_partnums(self.input):
            if foundone(coords, symset):
                total += partnum
        return total




    @answer(75312571)
    def part_2(self) -> int:
        def coord_partnum_dict():
            D = {}
            for partnum, coords in self.iter_poss_partnums(self.input):
                for rc in coords:
                    D[rc] = partnum
            return D
        
        def iter_start_coords():
            for r, line in enumerate(self.input):
                for m in re.finditer(r"\*", line):
                    yield r, m.start()
        cpd = coord_partnum_dict()
        star_neighbors = defaultdict(set)
        for rc in iter_start_coords():
            for nabe in self.neighbor(rc):
                partnum = cpd.get(nabe)
                if partnum is not None:
                    star_neighbors[rc].add(partnum)
        return sum(math.prod(xs) for xs in star_neighbors.values() if len(xs) == 2)



    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
