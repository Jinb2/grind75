from typing import *

# Solution : use hashmap and check difference


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        differences = {}

        for i in range(len(nums)):

            difference = target - nums[i]

            if difference in differences:
                return [i, differences[nums[i]]]

            differences[nums[i]] = i


# edge cases
solution = Solution()
solution.twoSum([0, 1, 2, 3], 2)  # return 0 and 1
