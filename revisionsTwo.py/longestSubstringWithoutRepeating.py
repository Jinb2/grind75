class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # brute force this we can check every possible combination
        # but there is repeated work O(n^2)
        # instead sliding window
        # use a set to keep track of char we seen
        # if we run into dupes we need to keep on moving left pointer till that char doesnt exist anymore

        if not s:
            return 0
        seen = set()
        l = 0

        maxLen = 0

        for r in range(len(s)):

            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])

            maxLen = max(maxLen, r - l + 1)

        return maxLen
