class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # use a set to store the numbers we've seen already for row and col
        # squares set

        row, col, squares = defaultdict(set), defaultdict(set), defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board)):

                if board[r][c] == ".":
                    continue

                val = board[r][c]

                if val in row[r] or val in col[c] or val in squares[(r // 3, c // 3)]:
                    return False

                row[r].add(val)
                col[c].add(val)
                squares[(r // 3, c // 3)].add(val)

        return True
