class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        maxArea = 0
        stack = []  # pair height index

        for i, h in enumerate(heights):

            start = i

            # heights are increasing
            while stack and stack[-1][1] > h:

                index, height = stack.pop()

                # compute if this is potential max area
                maxArea = max(maxArea, height * (i - index))

                start = index

            stack.append((start, h))

        for i, h in stack:

            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea
