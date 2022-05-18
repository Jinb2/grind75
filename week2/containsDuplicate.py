class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        duplicates = {}

        for i in range(len(nums)):

            if nums[i] in duplicates:
                return True

            duplicates[nums[i]] = 1

        return False
