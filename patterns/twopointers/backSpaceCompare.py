from typing import *


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        stackS = []
        stackT = []

        for i in range(len(s)):

            if s[i] == "#" and stackS:
                stackS.pop()
            elif s[i] != "#":
                stackS.append(s[i])

        for i in range(len(t)):

            if t[i] == "#" and stackT:
                stackT.pop()
            elif t[i] != "#":
                stackT.append(t[i])

        return stackS == stackT


print(Solution().backspaceCompare("y#fo##f", "y#f#o##f"))

https://leetcode.com/problems/backspace-string-compare/discuss/585027/Python-O(N)-Time-O(1)-Space-Solution-or-Explained