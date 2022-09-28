class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # trade for time for space
        seen = {}

        for num in nums:

            if num in seen:
                return True

            seen[num] = 1 + seen.get(num, 0)

        return False
