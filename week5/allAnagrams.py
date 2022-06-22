from typing import *
from copy import deepcopy


class Solution:
    # brute force way
    def findAnagrams(self, s: str, p: str) -> List[int]:

        res = []
        frequency = {}

        for c in p:

            if c not in frequency:
                frequency[c] = 0

            frequency[c] += 1

        for i in range(len(s)):

            copy = deepcopy(frequency)

            if i + len(p) > len(s):
                break
            elif s[i] not in frequency:
                continue
            else:

                for j in range(i, i + len(p)):

                    if s[j] not in copy:
                        break

                    copy[s[j]] -= 1

                if all(value == 0 for value in copy.values()):
                    res.append(i)

        return res


# solution = Solution()
# print(solution.findAnagrams(s="cbaebabacd", p="abc"))

# print(solution.findAnagrams(s="abab", p="ab"))


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p) > len(s):
            return []

        pCount = {}
        sCount = {}

        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)

        res = [0] if sCount == pCount else []

        l = 0

        for r in range(len(p), len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            sCount[s[l]] -= 1

            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l += 1

            if sCount == pCount:
                res.append(l)

        return res
