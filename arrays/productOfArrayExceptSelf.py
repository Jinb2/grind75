class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # a seperate ans array
        # calculate the pre prod and then calculate the post prod
        # do two pass
        # [1,2,3,4] nums
        # [1,1,1,1]
        # preProd = 6
        # reverse traversal
        # postProd = 24
        # [24,12,8,6]
        # [1,2,3,4] nums
        # two pass

        res = [1] * len(nums)

        # calculate pre product
        preProd = 1

        for i in range(len(nums)):
            res[i] = preProd
            preProd *= nums[i]

        postProd = 1

        for i in range(len(nums) - 1, -1, -1):

            res[i] *= postProd
            postProd *= nums[i]

        return res
