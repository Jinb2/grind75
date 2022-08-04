class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        # mark the seen numbers
        for n in nums:

            i = abs(n) - 1
            nums[i] = abs(nums[i]) * -1

        res = [i + 1 for i in range(len(nums)) if nums[i] > 0]

        return res
