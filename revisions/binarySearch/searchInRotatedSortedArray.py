class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # O(n) which is brute force just iterate over the nums
        # O(logn)
        # we can do this by figuring out which portion of the array we are in
        # left and right sorted portions
        # we can figure out which portion we are by comparing when we do binary search
        # middle value to the last element
        # and from there we can just run binary search

        l, r = 0, len(nums) - 1

        while l <= r:

            mid = (l + r) // 2

            # we return the index
            if nums[mid] == target:
                return mid

            # figure out which portion we are in
            if nums[mid] >= nums[r]:
                # left portion

                # search left
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:

                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
