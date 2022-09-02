class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return []

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:

            if leftMax < rightMax:

                # calculate trapwater at this index
                trapWater = leftMax - height[l]

                # if not negative add to curr val
                if trapWater > 0:
                    res += trapWater
                # increment
                l += 1
                # recalculate the max
                leftMax = max(leftMax, height[l])

            else:

                # calculate trapwater at this index
                trapWater = rightMax - height[r]

                if trapWater > 0:
                    res += trapWater
                r -= 1
                rightMax = max(rightMax, height[r])

        return res
