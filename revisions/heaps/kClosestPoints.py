import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # simple heap problem
        # use a max heap and add elements to heap
        # O(nlogn)
        # non trivial optimization
        # we can keep track of k largest elements so far
        # everytime our heap exceeds k we pop and then
        # [4,3,5]
        # -5,-4,-3

        heap = []

        for x, y in points:

            dist = -(x**2 + y**2)
            heapq.heappush(heap, (dist, x, y))

            if len(heap) > k:
                heapq.heappop(heap)

        return [[x, y] for _, x, y in heap]
