class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:

            # slight optimization
            # if already sorted
            if nums[l] < nums[r]:
                return min(res, nums[l])

            mid = (l + r) // 2
            res = min(res, nums[mid])

            # check which portion we are in
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1

        return res
