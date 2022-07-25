from typing import *
from unittest import skip


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

    def optimized(self, s, t):

        i, j = len(s) - 1, len(t) - 1

        skipS = 0
        skipT = 0

        while i >= 0 or j >= 0:

            while i >= 0:

                if s[i] == "#":
                    skipS += 1
                    i -= 1

                elif skipS > 0:
                    skipS -= 1
                    i -= 1

                else:
                    break

            while j >= 0:

                if s[i] == "#":
                    skipT += 1
                    j -= 1

                elif skipT > 0:

                    skipT -= 1
                    j -= 1

                else:
                    break

            if i >= 0 and j >= 0 and s[i] != s[j]:
                return False

            if (i >= 0) != (j >= 0):
                return False

            i = i - 1
            j = j - 1

        return True


print(Solution().backspaceCompare("y#fo##f", "y#f#o##f"))

# https://leetcode.com/problems/backspace-string-compare/discuss/585027/Python-O(N)-Time-O(1)-Space-Solution-or-Explained
