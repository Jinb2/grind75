from typing import *


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # what qualifies as a solution
        # just a subset
        # no dupes, we can keep track of an index of the number we are at
        # store possible candidates and we just use an array
        # what is our stopping condition? well after we use all the numbers
        # iterate through the array using dfs (subset,i)
        # after we get a candidate we want to remove the num we just added
        # at each sort of decision we have to choose whether or not we want to add the number or skip it

        res = []

        def backtrack(subset, i):

            if i == len(nums):
                res.append(
                    subset[::]
                )  # we want deepycopy because it can change through recursive calls
                return

            # we have the choice of appending and not appending
            # [1,2,3] [1,2]
            subset.append(nums[i])
            backtrack(subset, i + 1)
            subset.pop()
            backtrack(subset, i + 1)

        backtrack([], 0)

        return res


print(Solution().subsets([1, 2, 3]))
