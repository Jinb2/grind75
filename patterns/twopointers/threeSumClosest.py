class Solution:
    def threeSumClosest(self, nums, target):

        if len(nums) == 3:
            return sum(nums)

        nums.sort()
        closestSum = sum(nums[:3])

        for i, a in enumerate(nums):

            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:

                threeSum = a + nums[l] + nums[r]

                if abs(target - threeSum) < abs(target - closestSum):
                    closestSum = threeSum

                if threeSum > target:
                    r -= 1
                elif threeSum < target:
                    l += 1
                else:
                    return closestSum

        return closestSum


print(Solution().threeSumClosest([-1, 2, 1, -4], 1))

print(Solution().threeSumClosest([0, 0, 0], 1))
