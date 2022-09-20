class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # Time complexity O(n*m*4^n)
        # memory is going to be same because we are using recursive calls

        rows, cols = len(board), len(board[0])

        # can use a hashset but we can optimize by just marking the board and then unmarking it
        def dfs(r, c, i):

            # when i == len(word) meaning word has been found
            if i == len(word):
                return True

            # when is it not valid
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
                return False

            temp = board[r][c]  # store this value
            board[r][c] = "#"

            # explore all four directions
            res = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )

            # make sure to unmark it
            board[r][c] = temp

            return res

        for row in range(rows):
            for col in range(cols):

                if board[row][col] == word[0]:

                    if dfs(row, col, 0):
                        return True

        return False
