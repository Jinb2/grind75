# Solution: Hashmap


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        charOfS = {}
        charOfT = {}

        for i in range(len(s)):
            charOfS[s[i]] = 1 + charOfS.get(s[i], 0)

        for i in range(len(t)):
            charOfT[t[i]] = 1 + charOfT.get(t[i], 0)

        return charOfS == charOfT


solution = Solution()
print("True", solution.isAnagram("anagram", "nagaram"))
print("False", solution.isAnagram("rat", "car"))
print("True", solution.isAnagram("", ""))
print("False", solution.isAnagram("ratf", "car"))
