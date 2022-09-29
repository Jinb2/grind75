class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        res = []
        while k > 0:

            k -= 1

            maxNum = max(count, key=count.get)
            del count[maxNum]
            res.append(maxNum)

        return res

    def bucketSort(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, count in count.items():

            bucket[count].append(num)

        res = []
        # reverse

        for i in range(len(bucket) - 1, -1, -1):

            if bucket[i]:

                for num in bucket[i]:
                    k -= 1
                    res.append(num)

                    if k == 0:
                        return res
