from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # for sudoku we just need to make sure a row doesnt contain dupes, col doesnt contain dupes and a 3x3 doent contain dupes
        # so we have O(81) for space time and runtime
        rows = defauldict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board)):

                if board[r][c] == ".":
                    continue

                # stop condition
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
