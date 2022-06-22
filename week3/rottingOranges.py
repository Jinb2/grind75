class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q = deque()
        time, fresh = 0, 0

        ROWS, COLS = len(grid), len(grid[0])

        for row in range(ROWS):
            for col in range(COLS):

                if grid[row][col] == 1:
                    fresh += 1

                if grid[row][col] == 2:
                    q.append([row, col])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while q and fresh > 0:

            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = dr + r, dc + c

                    if (
                        row not in range(ROWS)
                        or col not in range(COLS)
                        or grid[row][col] != 1
                    ):
                        continue
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1

            time += 1

        return time if fresh == 0 else -1