class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        freq = set()

        l = 0
        maxLen = 0

        for r in range(len(s)):

            while s[r] in freq:
                freq.remove(s[r])
                l += 1

            freq.add(s[r])

            maxLen = max(maxLen, r - l + 1)

        return maxLen
