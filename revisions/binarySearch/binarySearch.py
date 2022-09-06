class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # O(logn) we use two pointers and divide search

        l,r = 0, len(nums) - 1

        while l <= r:

            mid = (l+r) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1

