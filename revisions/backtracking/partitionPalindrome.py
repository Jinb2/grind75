class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        part = []

        # at each iteration we are partitioning

        def backtrack(i):

            if i >= len(s):
                res.append(part[::])
                return
            # i stays same but j increases
            for j in range(i, len(s)):

                if self.isPali(s, i, j):
                    part.append(s[i : j + 1])
                    backtrack(j + 1)
                    part.pop()

        backtrack(0)

        return res

    def isPali(self, s, l, r):

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True
