import collections


class Solution:
    def shortestPath(self, grid):

        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        visited = set()

        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == "*":
                    q.append((row, col, 0))
                    visited.add((row, col))
                    break

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:

            r, c, steps = q.popleft()

            if grid[r][c] == "#":
                return steps

            for x, y in directions:

                row, col = r + x, c + y

                if (
                    (0 <= row < rows)
                    and (0 <= col < cols)
                    and (row, col) not in visited
                    and grid[row][col] != "X"
                ):
                    q.append((row, col, steps + 1))
                    visited.add((row, col))

        return -1


print(
    Solution().shortestPath(
        [
            ["X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "*", "O", "X", "O", "#", "O", "X"],
            ["X", "O", "O", "X", "O", "O", "X", "X"],
            ["X", "O", "O", "O", "O", "#", "O", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X"],
        ]
    )
)
