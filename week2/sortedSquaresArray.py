from typing import *


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        answer = [0] * len(nums)

        l, r = 0, len(nums) - 1

        while l <= r:

            left, right = abs(nums[l]), abs(nums[r])

            if left > right:
                answer[r - l] = left * left
                l += 1
            else:
                answer[r - l] = right * right
                r -= 1

        return answer
