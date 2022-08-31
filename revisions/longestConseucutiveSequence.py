class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # we can mark the start of sequence as the num - 1 not existing in the array
        # O(n) space and runtime

        maxLen = 0
        numSet = set(nums)

        for num in nums:

            if (num - 1) not in numSet:
                length = 0

                while num in numSet:
                    num += 1
                    length += 1

                maxLen = max(length, maxLen)

        return maxLen
