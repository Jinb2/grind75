class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        sMap = {}
        tMap = {}

        for i in range(len(s)):

            # f : b  b : f
            # o : a a : o
            # o : r r : o

            charS = s[i]
            charT = t[i]

            if charS in sMap and sMap[charS] != charT:
                return False

            if charT in tMap and tMap[charT] != charS:
                return False

            sMap[charS] = charT
            tMap[charT] = charS

        return True
