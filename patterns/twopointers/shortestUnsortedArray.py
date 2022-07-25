from typing import *


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        start, end = 0, 0

        minNum, maxNum = nums[-1], nums[0]

        for l in range(1, len(nums)):

            if nums[l] < maxNum:
                end = l
            else:
                maxNum = nums[l]

        for r in range(len(nums) - 1, -1, -1):

            if nums[r] > minNum:
                start = r
            else:
                minNum = nums[r]

        return 0 if start == end else end - start + 1


print(Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))

print(Solution().findUnsortedSubarray([1, 2, 3, 4]))
