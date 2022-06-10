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
