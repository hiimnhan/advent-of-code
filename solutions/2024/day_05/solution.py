# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/5

from ...base import StrSplitSolution, answer
import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10000)


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.topo_order = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def print_graph(self):
        for node in self.graph:
            print(node, " -> ", self.graph[node])

    def topo_sort(self):
        indegree = defaultdict(int)
        queue = deque()

        for node in self.graph:
            if node not in indegree:
                indegree[node] = 0
            for neighbour in self.graph[node]:
                indegree[neighbour] += 1
        print(indegree)

        for node in self.graph:
            if indegree[node] == 0:
                queue.append(node)

        print(queue)
        while queue:
            node = queue.popleft()
            print(node)
            self.topo_order.append(node)

            for neighbour in self.graph[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        print(self.topo_order)

    def is_subarray_topo(self, array):
        for i in range(1, len(array)):
            if self.topo_order.index(array[i - 1]) > self.topo_order.index(array[i]):
                return False
        return True


class Solution(StrSplitSolution):
    _year = 2024
    _day = 5

    ordering_rules = []
    pages = []
    graph = Graph()

    def init(self):
        for line in self.input:
            if "|" in line:
                first, second = line.split("|")
                self.ordering_rules.append((int(first), int(second)))
            elif "," in line:
                self.pages.append([int(x) for x in line.split(",")])
        for first, second in self.ordering_rules:
            self.graph.add_edge(first, second)
        # print(self.ordering_rules)

    # @answer(1234)
    def part_1(self) -> int:
        ans = 0
        self.init()
        self.graph.print_graph()
        self.graph.topo_sort()
        # for page in self.pages:
        #     if self.graph.is_subarray_topo(page):
        #         middle_index = len(page) // 2
        #         ans += page[middle_index]
        return ans

    # @answer(1234)
    def part_2(self) -> int:
        pass
