class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        # use set to store which cols dont need for row because we know only one per row
        cols = set()

        # r+c because row dec and col inc
        posDiag = set()

        # r-c because row inc and col dec
        negDiag = set()

        res = []

        board = [["."] * n for i in range(n)]

        # we only need row since we know queens have to be in diff row
        def backtrack(r):

            # goal
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            # otherwise our search is to search every c
            for c in range(n):

                # invalid candidate
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                # make sure to add this to combination
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"
                backtrack(r + 1)

                # we need to abandon the candidates
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)

        return res
