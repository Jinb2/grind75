class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        res = []

        def backtrack(i, comb, currSum):

            # goal of the backtrack
            if currSum == target:
                res.append(comb[::])
                return

            # now lets get into edge cases where we dont want to keep searching
            if i == len(candidates) or currSum > target:
                return

            # we always have to decisions the first being that we choose to stay at this current num
            comb.append(candidates[i])
            backtrack(i + 1, comb, currSum + candidates[i])

            # we want to not pick this number
            comb.pop()

            # we have to deal with some duplicates
            if i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            backtrack(i + 1, comb, currSum)

        backtrack(0, [], 0)

        return res
