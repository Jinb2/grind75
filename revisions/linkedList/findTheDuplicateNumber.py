class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # so we can brute force just iterate through array and find it
        # another way is to use cyclic sorting O(n) essentially we mark seen elements to their respective index
        # the reason this works is because we know numbers [1,n+1]

        # linked list way is to use fast and slow
        # have slow and fast meet
        # then we use antohe rslow pointer to meet

        slow, fast = nums[0], nums[nums[0]]

        while slow != fast:

            slow = nums[slow]
            fast = nums[nums[fast]]

        # now we start from begining and iterate again
        slow2 = nums[0]

        while slow2 != slow:

            slow2 = nums[slow2]
            slow = nums[slow]

        return slow
