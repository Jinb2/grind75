class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        # same as subset one but we need to deal with duplicates
        # to deal with dupes just sort array and skip it if same as previous

        nums.sort()
        res = []

        def backtrack(i, sub):

            if i == len(nums):
                res.append(sub[::])
                return

            # add the number or skip it
            sub.append(nums[i])
            backtrack(i + 1, sub)

            # dont include
            sub.pop()

            # skip duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            backtrack(i + 1, sub)

        backtrack(0, [])
        return res
