class Solution:
    def maxArea(self, height: List[int]) -> int:

        maxArea = 0
        l, r = 0, len(height) - 1

        while l < r:

            width = r - l
            currHeight = min(height[l], height[r])
            currArea = width * currHeight
            maxArea = max(maxArea, currArea)

            if height[l] < height[r]:
                l += 1
            elif height[r] < height[l]:
                r -= 1
            else:
                l += 1

        return maxArea
