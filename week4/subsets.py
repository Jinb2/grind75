from typing import *


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        curr = []

        def subset(i):

            if i >= len(nums):
                res.append(curr[::])
                return

            curr.append(nums[i])
            subset(i + 1)

            curr.pop()
            subset(i + 1)

        subset(0)

        return res


solution = Solution()
print(solution.subsets([1, 2, 3]))
