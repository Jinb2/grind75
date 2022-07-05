from collections import Counter
import heapq
from typing import *


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        # gets count of each word
        # word : count
        counter = Counter(words)
        count = {}

        print(counter)

        # group words by frequency
        for i in counter:
            if counter[i] not in count:
                count[counter[i]] = [i]
            else:
                count[counter[i]].append(i)

        heapcount = list(count.keys())
        heapq._heapify_max(heapcount)

        output = []

        while k > 0:
            v = heapq._heappop_max(heapcount)

            temp = []
            for i in count[v]:
                temp.append(i)

            heapq.heapify(temp)  # help sort lexographically

            while len(temp) > 0:

                output.append(heapq.heappop(temp))
                k -= 1
                if k == 0:
                    return output

        return output


print(Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 3))
