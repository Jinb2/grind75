class Solution:
    def findDuplicate(self, nums: List[int]) -> List[int]:

        i = 0

        while i < len(nums):

            n = nums[i]

            if n == i + 1:
                i += 1
            else:

                idx = n - 1

                if nums[idx] == idx + 1:
                    return idx + 1

                nums[i], nums[idx] = nums[idx], nums[i]
