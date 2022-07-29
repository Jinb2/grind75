class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:

        n = len(nums)

        for i, num in enumerate(nums):

            linkLength = 0
            j = i

            forward = nums[j] > 0

            while True:

                if (forward and nums[j] < 0) or (not forward and nums[j] > 0):
                    break

                nextJ = (j + nums[j] + n) % n

                if j == nextJ:
                    break

                j = nextJ
                linkLength += 1

                if linkLength > n:
                    return True

        return False
