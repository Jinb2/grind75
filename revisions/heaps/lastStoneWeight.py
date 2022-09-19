import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # heapify our stones
        # we want a max heap
        for i, s in enumerate(stones):
            stones[i] = -s

        heapq.heapify(stones)

        # keep popping till no more stones are left
        while stones:

            s1 = -heapq.heappop(stones)

            # if no more stones return
            if not stones:
                return s1

            s2 = -heapq.heappop(stones)

            # now lets compare
            if s1 > s2:
                heapq.heappush(stones, s2 - s1)

        return 0
