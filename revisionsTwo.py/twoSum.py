class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # hashmap [val] = i
        # x + y = target
        # x = target - y

        seen = {}

        for i in range(len(nums)):

            difference = target - nums[i]

            if difference in seen:
                return [i, seen[difference]]

            seen[nums[i]] = i
