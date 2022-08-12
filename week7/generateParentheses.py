class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # add open if open < n
        # add closed if close < open
        # append when closed = open = n

        stack = []
        res = []

        def backtrack(openN, closedN):

            # base case
            if openN == closedN == n:
                res.append("".join(stack))
                return

            # have to append "(" first and then
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:

                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)

        return res
