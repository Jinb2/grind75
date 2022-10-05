class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(s) > len(t):
            return False

        if not s:
            return True

        # pos of s we are at
        i = 0

        for c in t:

            if c == s[i]:
                i += 1

            if i == len(s):
                return True

        return False
