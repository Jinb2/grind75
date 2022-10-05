class Solution:
    def trap(self, height: List[int]) -> int:

        # the water height is limited by the minimum height of left and right
        # water trapped is min(leftH,rightH) - height[i]
        # we can have two arrays to keeptrack fo left minHeight and right minHeight
        # then just compute min(leftH,rightH) - height[i] at every point

        leftMax = [0] * len(height)
        rightMax = [0] * len(height)

        # calculate leftMax
        for i in range(1, len(height)):

            leftMax[i] = max(leftMax[i - 1], height[i])

        for i in range(len(height) - 2, -1, -1):

            rightMax[i] = max(rightMax[i + 1], height[i])

        ans = 0

        for i in range(len(height)):

            ans += max(0, min(leftMax[i], rightMax[i]) - height[i])

        return ans
