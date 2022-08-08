class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        for i in range(len(nums)):

            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):

            value = abs(nums[i])

            if 1 <= value <= len(nums):
                # mark as seen
                if nums[value - 1] > 0:
                    nums[value - 1] *= -1
                elif nums[value - 1] == 0:
                    nums[value - 1] = -1 * (len(nums) + 1)

        # iterate through 1 to n + 1

        for i in range(1, len(nums) + 1):

            # never seen
            if nums[i - 1] >= 0:
                return i

        return len(nums) + 1
