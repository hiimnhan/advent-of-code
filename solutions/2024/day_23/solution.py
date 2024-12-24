# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/23

from solutions.utils.graph import count_cycles, init_network
from ...base import StrSplitSolution, answer
import sys
from collections import defaultdict
import networkx as nx

sys.setrecursionlimit(10000)


class Solution(StrSplitSolution):
    _year = 2024
    _day = 23

    # @answer(1234)
    def part_1(self) -> int:
        ans = 0
        graph = defaultdict(set)
        with_t = set()
        for line in self.input:
            a, b = line.split("-")
            if a.startswith("t"):
                with_t.add(a)
            if b.startswith("t"):
                with_t.add(b)
            graph[a].add(b)
            graph[b].add(a)
        # print_graph(graph)
        # visualize_graph(graph)
        _, cycles = count_cycles(graph, 3)
        for c in cycles:
            if any(x in with_t for x in c):
                print(c)
                ans += 1
        return ans

    # @answer(1234)
    def part_2(self) -> int:
        ans = 0
        graph = defaultdict(set)
        for line in self.input:
            a, b = line.split("-")
            graph[a].add(b)
            graph[b].add(a)
        G = init_network(graph)
        biggest_cycle = []

        for clique in sorted(nx.find_cliques(G), key=lambda x: len(x), reverse=True):
            if len(clique) < len(biggest_cycle):
                continue
            clique = sorted(clique)
            if clique == biggest_cycle:
                continue

            for i in range(len(clique)):
                node = clique[i]
                to_check = clique[:i] + clique[i + 1 :]
                if not all(tc in graph[node] for tc in to_check):
                    break
            else:
                biggest_cycle = clique
        print(",".join(biggest_cycle))

        return ans
