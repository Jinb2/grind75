from typing import *


# sliding window typically works only for positive numbers or if it is sorted
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # prefix sum to count
        # reason being is can we chop off a portion of array to get the k
        prefixSum = {0: 1}
        res = 0
        currSum = 0

        for num in nums:

            currSum += num

            # this is the prefix we are looking for
            diff = currSum - k

            # if it exists add current count so far
            res += prefixSum.get(diff, 0)
            prefixSum[currSum] = 1 + prefixSum.get(currSum, 0)

        return res


print(Solution().subarraySum(nums=[1, 1, 1], k=2))
print(Solution().subarraySum(nums=[1, 2, 3], k=3))
