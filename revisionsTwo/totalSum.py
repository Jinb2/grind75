class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        # keep track of prefix sum we know that it equals if the
        # left sum equals remaining excluding the index we are at
        total = sum(nums)
        leftSum = 0

        for i, num in enumerate(nums):

            if leftSum == total - leftSum - num:
                return i

            leftSum += num

        return -1
