# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/2

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2024
    _day = 2

    def isIncreasing(self, nums):
        N = len(nums)
        return all(nums[i] - nums[i - 1] in (1, 2, 3) for i in range(1, N))

    def isDecreasing(self, nums):
        N = len(nums)
        return all(nums[i - 1] - nums[i] in (1, 2, 3) for i in range(1, N))

    def isSafeWithDampner(self, nums):
        if self.isIncreasing(nums) or self.isDecreasing(nums):
            return True
        N = len(nums)
        for i in range(N):
            modified = nums[:i] + nums[i + 1 :]
            if self.isIncreasing(modified) or self.isDecreasing(modified):
                return True
        return False

    @answer(359)
    def part_1(self) -> int:
        ans = 0
        for line in self.input:
            nums = [int(x) for x in line.split()]
            if self.isIncreasing(nums) or self.isDecreasing(nums):
                ans += 1

        return ans

    @answer(418)
    def part_2(self) -> int:
        ans = 0
        for line in self.input:
            nums = [int(x) for x in line.split()]
            if self.isSafeWithDampner(nums):
                ans += 1

        return ans

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
