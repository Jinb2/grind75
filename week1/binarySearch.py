# Solution hint: two pointer
from typing import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l <= r:

            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1


solution = Solution()
print("4", solution.search([-1, 0, 3, 5, 9, 12], 9))
print("-1", solution.search([-1, 0, 3, 5, 9, 12], 2))
print("0", solution.search([5], 5))
