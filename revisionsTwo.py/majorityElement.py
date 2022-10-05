class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # O(n) space and time

        n = floor(len(nums) // 2)

        freq = {}

        for num in nums:

            freq[num] = 1 + freq.get(num, 0)

        return max(freq, key=freq.get)
