class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS, COLS = len(board), len(board[0])

        def dfs(i, r, c):

            if i == len(word):
                return True

            # edge cases
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != word[i]:
                return False

            temp = board[r][c]
            board[r][c] = "#"

            res = (
                dfs(i + 1, r + 1, c)
                or dfs(i + 1, r - 1, c)
                or dfs(i + 1, r, c - 1)
                or dfs(i + 1, r, c + 1)
            )

            board[r][c] = temp

            return res

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] != word[0]:
                    continue
                elif dfs(0, row, col):
                    return True

        return False


solution = Solution()

print(
    solution.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="ABCCED",
    )
)

print(
    solution.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="SEE",
    )
)

print(
    solution.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="ABCB",
    )
)
