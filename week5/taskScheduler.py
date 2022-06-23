class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # hashmap
        count = Counter(tasks)
        # maxHeap
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pair [count, idleTime]

        while maxHeap or q:

            time += 1

            if maxHeap:
                # negative since its python
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    q.append([count, time + n])

            if q and q[0][1] == time:

                heapq.heappush(maxHeap, q.popleft()[0])

        return time
