import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        heapq.heapify(self.heap)

        # append neg
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:

        # so we first add to our stream
        heapq.heappush(self.heap, -val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return -1 * self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
