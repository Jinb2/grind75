class Solution:
    """
    Input: nums = [3,0,1]
    Output: 2

    Input: nums = [0,1]
    Output: 2

    Input: nums = [9,6,4,2,3,5,7,0,1]
    Output: 8
    """

    def missingNumber(self, nums: List[int]) -> int:

        # cyclic sorting

        i = 0

        while i < len(nums):
            j = nums[i]

            # swap to correct position
            if nums[i] < len(nums) and nums[i] != i:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        # list is sorted so now we can check for where it doesnt equal its index
        for i, num in enumerate(nums):
            if num != i:
                return i
        
        # if list is already sorted then its just the len of the nums
        # example [0,1]

        return len(nums)
