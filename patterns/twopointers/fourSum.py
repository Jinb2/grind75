from typing import *


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        if not nums or len(nums) < 4:
            return []

        nums.sort()
        res = []

        for i in range(len(nums) - 3):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums) - 2):

                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                sumA = nums[i] + nums[j]

                left = j + 1
                right = len(nums) - 1

                while left < right:

                    sumB = sumA + nums[left] + nums[right]

                    if target == sumB:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif sumB < target:
                        left += 1
                    else:
                        right -= 1

        return res


print(Solution().fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
