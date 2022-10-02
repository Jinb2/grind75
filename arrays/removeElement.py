class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0

        # we want to move all non remove target to front
        for i in range(len(nums)):

            # safe to move on since not a num we
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k
