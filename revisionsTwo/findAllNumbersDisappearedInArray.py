class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        seen = {}

        for num in nums:
            seen[num] = 1 + seen.get(num, 0)

        res = []
        for i in range(1, len(nums) + 1):

            if i not in seen:
                res.append(i)

        return res
