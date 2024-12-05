# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/5

from ...base import StrSplitSolution, answer
import sys
from collections import defaultdict, deque
from functools import cmp_to_key

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
    # graph = Graph()

    def check(self, line):
        for rule in self.ordering_rules:
            if rule[0] in line and rule[1] in line:
                if line.index(rule[0]) > line.index(rule[1]):
                    return False
        return True

    def cmp_func(self, a, b) -> int:
        for rule in self.ordering_rules:
            if rule[0] == a and rule[1] == b:
                return -1
            elif rule[0] == b and rule[1] == a:
                return 1
        return 0

    def init(self):
        for line in self.input:
            if "|" in line:
                first, second = line.split("|")
                self.ordering_rules.append((int(first), int(second)))
            elif "," in line:
                self.pages.append([int(x) for x in line.split(",")])

    # @answer(1234)
    def part_1(self) -> int:
        ans = 0
        self.init()
        for page in self.pages:
            if self.check(page):
                middle_index = len(page) // 2
                ans += page[middle_index]
        # self.graph.print_graph()
        # self.graph.topo_sort()
        # for page in self.pages:
        #     if self.graph.is_subarray_topo(page):
        #         middle_index = len(page) // 2
        #         ans += page[middle_index]
        return ans

    # @answer(1234)
    def part_2(self) -> int:
        ans = 0
        # self.init()
        for page in self.pages:
            if not self.check(page):
                print(page)
                update = sorted(page, key=cmp_to_key(self.cmp_func))
                print(update)
                middle_index = len(update) // 2
                ans += update[middle_index]
        return ans
