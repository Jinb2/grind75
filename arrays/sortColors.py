class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # get num of 1s 2s and 0s
        # and then just replace the values acoordingly
        l, r = 0, len(nums) - 1
        i = 0

        while i <= r:

            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1
            elif nums[i] == 2:
                # dont increment i because we dont know anything about nums after i
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
            else:
                i += 1
