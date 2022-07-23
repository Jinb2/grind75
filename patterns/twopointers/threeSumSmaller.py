class Solution:
    def three_sum_smaller(self, nums, target):

        if len(nums) < 3:
            return 0

        nums.sort()
        numSmaller = 0

        for i, a in enumerate(nums):

            l, r = i + 1, len(nums) - 1

            while l < r:

                threeSum = a + nums[l] + nums[r]

                if threeSum < target:
                    numSmaller += (
                        r - l
                    )  # since r is the largest value the indexes before would also be less than target
                    l += 1
                elif threeSum >= target:
                    r -= 1

        return numSmaller
