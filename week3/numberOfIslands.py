class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])

        islands = 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            grid[r][c] = "#"
            while q:
                row, col = q.popleft()
                dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for x, y in dirs:
                    r, c = row + x, col + y
                    if (r in range(rows)) and (c in range(cols)) and grid[r][c] == "1":
                        q.append((r, c))
                        grid[r][c] = "#"

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands


# no queue needed version
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        numIslands = 0

        def bfs(r, c):
            grid[r][c] = "#"
            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for x, y in dirs:
                row = r + x
                col = c + y
                if row in range(ROWS) and col in range(COLS) and grid[row][col] == "1":
                    bfs(row, col)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    bfs(row, col)
                    numIslands += 1

        return numIslands
