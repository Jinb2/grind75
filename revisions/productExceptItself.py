class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # brute force is have two loops that calculates running product for each element
        # O(n^2)

        # we can reduce by using prefix and postfix product
        # because essentially that is what the question is asking
        # O(n) space

        # calculate the pre product
        preProd = 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = preProd
            preProd *= nums[i]

        postProd = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postProd
            postProd *= nums[i]

        return res
