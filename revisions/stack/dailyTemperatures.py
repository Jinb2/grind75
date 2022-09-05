class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        stack = []  # temps in decreasing order (index,temp)

        for i, temp in enumerate(temperatures):

            # so maintain decreasing order
            while stack and stack[-1][1] < temp:

                idx, t = stack.pop()
                res[idx] = i - idx

            stack.append([i, temp])

        return res
