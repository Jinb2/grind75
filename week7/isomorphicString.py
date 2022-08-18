class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        # two hashmaps
        # map them to each other
        # if at any point the matchings dont match with the curr char return false
        # O(n) time and Space

        mapST, mapTS = {}, {}

        for i in range(len(s)):

            c1, c2 = s[i], t[i]

            if (c1 in mapST) and mapST[c1] != c2 or (c2 in mapTS and mapTS[c2] != c1):
                return False

            mapST[c1] = c2
            mapTS[c2] = c1

        return True
