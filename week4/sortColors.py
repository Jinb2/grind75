class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l, r = 0, len(nums) - 1

        i = 0

        while i <= r:
            # reason we dont move i if it is a "2" is because r > i and we dont know what values exist after it
            # where as for l we do know -> always 0
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
            else:
                i += 1
