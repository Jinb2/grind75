class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # realize that since its sorted either ends of the list will be greatest value

        res = []

        l, r = 0, len(nums) - 1

        while l <= r:

            if abs(nums[l]) > abs(nums[r]):
                sq = nums[l] * nums[l]
                res.append(sq)
                l += 1
            else:
                sq = nums[r] * nums[r]
                res.append(sq)
                r -= 1

        return res[::-1]
