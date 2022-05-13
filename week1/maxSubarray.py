# Solution: global min and max
from typing import *


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSum, currSum = nums[0], 0

        for i in range(len(nums)):

            currSum = max(currSum + nums[i], nums[i])
            maxSum = max(currSum, maxSum)

        return maxSum


solution = Solution()
print("6", solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print("1", solution.maxSubArray([1]))
print("23", solution.maxSubArray([5, 4, -1, 7, 8]))
print("-1", solution.maxSubArray([-1]))
