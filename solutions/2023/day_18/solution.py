# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/18


from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 18

    @answer(48795)
    def part_1(self) -> int:
        points = [(0, 0)]

        directions = {
            "U": (-1, 0),
            "D": (1, 0),
            "L": (0, -1),
            "R": (0, 1)
        }

        b  = 0
        
        for line in self.input:
            d, n, _ = line.split()
            dr, dc = directions[d]
            n = int(n)
            b += n
            r, c = points[-1]
            points.append((r + dr * n, c + dc * n))

        N = len(points)
        A = abs(sum(points[i][0] * (points[i - 1][1] - points[(i + 1) % N ][1]) for i in range(N))) // 2 # Shoelace formula

        i = A  - b // 2 + 1 # Pick's theorem

        return i + b






    @answer(40654918441248)
    def part_2(self) -> int:
        points = [(0, 0)]

        directions = {
            "U": (-1, 0),
            "D": (1, 0),
            "L": (0, -1),
            "R": (0, 1)
        }

        parse_d = {
            0: 'R',
            1: 'D',
            2: 'L',
            3: 'U'
        }

        b  = 0
        
        for line in self.input:
            _, _, code = line.split()
            code = code.replace('(', '').replace(')', '').replace('#', '')
            d = parse_d[int(code[-1])]
            n = int(code[:5], 16)
            b += n
            dr, dc = directions[d]
            r, c = points[-1]
            points.append((r + dr * n, c + dc * n))

        N = len(points)
        A = abs(sum(points[i][0] * (points[i - 1][1] - points[(i + 1) % N ][1]) for i in range(N))) // 2 # Shoelace formula

        i = A  - b // 2 + 1 # Pick's theorem

        return i + b

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
