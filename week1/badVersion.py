# Solution hint : Binary search


class Solution:
    def firstBadVersion(self, n: int) -> int:

        # boundaries
        l, r = 1, n

        while l < r:

            mid = (l + r) // 2

            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1

        return l
