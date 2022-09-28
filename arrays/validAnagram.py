class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for i in range(len(s)):

            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT

        # O(n+m) for space and time
        # anagram is when you can rearrange one string to form anothr
        # use hashmap to keep track of th numbr of characters in each

        return countS == countT
