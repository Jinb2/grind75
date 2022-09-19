class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # [1,2,3,4] target = 7
        # [1,1,1,1,1,1,1,1], [2,2,2,1],[2,2,3][1,1,2,3] [4,3]
        # its whether or not we keep adding this number or we move on to the next number
        # [1,1]
        # either the sum is too big or it meets the target or we are out of bounds
        # apepnd when target meet sthe value
        # pointer, keep track of currsum

        res = []

        def backtrack(i, comb, currSum):

            if currSum == target:
                res.append(comb[::])
                return

            # cases to stop searching
            if candidates[i] > target or i == len(candidates):
                return

            # two choices add this number or skip
            comb.append(candidates[i])
            backtrack(i, comb, currSum + candidates[i])
            comb.pop()
            backtrack(i + 1, comb, currSum)

        backtrack(0, [], 0)

        return res
