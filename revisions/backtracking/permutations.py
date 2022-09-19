class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []  # returning the permutation

        if len(nums) == 1:
            return [nums[::]]

        # [1,2,3] [1,2,3]

        # go through each number

        for _ in range(len(nums)):

            n = nums.pop(
                0
            )  # pop first element because if we pop last element we just get same permutation
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)

            res.extend(perms)
            nums.append(n)

        return res
