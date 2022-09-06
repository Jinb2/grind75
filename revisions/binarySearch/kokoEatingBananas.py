class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # a brute force way is too just to check hours neede from 1 to max of piles
        # O(n^2) since we have to do a pass for each element

        # a better way to do this is we can binary search from 1 to max of piles
        # O(n*log(max(piles))))

        l, r = 1, max(piles)

        res = r

        while l <= r:

            k = (l + r) // 2

            # for this k how many hours
            hours = 0

            for p in piles:
                # round up
                hours += math.ceil(p / k)

            # are not eating a rate that is too slow
            if hours <= h:
                res = min(k, res)
                r = k - 1
            else:  # takes too long to eat so we gotta increase our k
                l = k + 1

        return res
