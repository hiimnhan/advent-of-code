# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/16

from collections import deque

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 16


    @answer(7979)
    def part_1(self) -> int:
        seen = set()
        R = len(self.input)
        C = len(self.input[0])
        directions = [
            (1, 0), #D
            (0, 1), #R
            (-1, 0), #U
            (0, -1) #L
        ]

        q = deque()
        q.append((0, 0, 0))
        seen.add((0, 0, 0))

        def add(t):
            if t not in seen:
                seen.add(t)
                q.append(t)

        while len(q):
            x, y, d = q.popleft()
            dx, dy = directions[d]

            nx, ny = x + dx, y + dy

            if 0 <= nx < R and 0 <= ny < C:
                if self.input[nx][ny] == '.':
                    t = (nx, ny, d)
                    add(t)
                elif self.input[nx][ny] == '\\':
                    t = (nx, ny, d ^ 1)
                    add(t)
                elif self.input[nx][ny] == '/':
                    t = (nx, ny, d ^ 3)
                    add(t)
                elif self.input[nx][ny] == '|':
                    if d in [1, 3]:
                        for nd in [0, 2]:
                            t = (nx, ny, nd)
                            add(t)
                    else:
                        t = (nx, ny, d)
                        add(t)
                elif self.input[nx][ny] == '-':
                    if d in [0, 2]:
                        for nd in [1, 3]:
                            t = (nx, ny, nd)
                            add(t)
                    else:
                        t = (nx, ny, d)
                        add(t)
        seen2 = set()
        for x, y, d in seen:
            seen2.add((x, y))

        return len(seen2)

    # @answer(8437)
    def part_2(self) -> int:
        R = len(self.input)
        C = len(self.input[0])

        def solve(sx, sy, nd):
            seen = set()
            directions = [
                (1, 0), #D
                (0, 1), #R
                (-1, 0), #U
                (0, -1) #L
            ]

            q = deque()
            q.append((sx, sy, nd))

            def add(t):
                if t not in seen:
                    seen.add(t)
                    q.append(t)

            while len(q):
                x, y, d = q.popleft()
                dx, dy = directions[d]

                nx, ny = x + dx, y + dy

                if 0 <= nx < R and 0 <= ny < C:
                    if self.input[nx][ny] == '.':
                        t = (nx, ny, d)
                        add(t)
                    elif self.input[nx][ny] == '\\':
                        t = (nx, ny, d ^ 1)
                        add(t)
                    elif self.input[nx][ny] == '/':
                        t = (nx, ny, d ^ 3)
                        add(t)
                    elif self.input[nx][ny] == '|':
                        if d in [1, 3]:
                            for nd in [0, 2]:
                                t = (nx, ny, nd)
                                add(t)
                        else:
                            t = (nx, ny, d)
                            add(t)
                    elif self.input[nx][ny] == '-':
                        if d in [0, 2]:
                            for nd in [1, 3]:
                                t = (nx, ny, nd)
                                add(t)
                        else:
                            t = (nx, ny, d)
                            add(t)
            seen2 = set()
            for x, y, d in seen:
                seen2.add((x, y))

            return len(seen2)
        best = 0
        for x in range(R):
            best = max(best, solve(x, -1, 1))
            best = max(best, solve(x, C + 1, 3))

        for y in range(C):
            best = max(best, solve(-1, y, 0))
            best = max(best, solve(R, y, 2))

        return best
                



    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
