class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(n)
        # so we can use bucket sort
        # use a hashmap that stores the value as such
        # count : number with that count
        count = {}
        # use the index as the count since max count is len of array
        freq = [[] for _ in range(len(nums) + 1)]
        res = []

        # get the count of each num
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # now we append to our hashmap
        for n, c in count.items():
            freq[c].append(n)

        # now start from reverse
        for i in range(len(freq) - 1, 0, -1):

            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
