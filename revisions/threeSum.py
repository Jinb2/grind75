class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # brute force is O(n^3) we check every possibility for every element
        # we can sort it and make the run time O(n^2) sorting takes o(nlogn)
        # we sort then break the problem into two sum  two but we need to account for duplicates

        nums.sort()
        res = []

        for i, a in enumerate(nums):

            # to account for dupes check if prev number exists
            if i > 0 and a == nums[i - 1]:
                continue

            # otherwise we do two sum
            l = i + 1
            r = len(nums) - 1

            while l < r:

                totalSum = a + nums[r] + nums[l]

                if totalSum > 0:
                    r -= 1
                elif totalSum < 0:
                    l += 1
                else:
                    res.append([a, nums[r], nums[l]])
                    l += 1
                    # [2,2,0,0,-2,-2]
                    # now we could have dupes
                    # we will just move left because our if and else will account for this
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res
