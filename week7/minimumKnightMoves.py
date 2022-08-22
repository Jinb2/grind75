from collections import deque


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:

        # (x,y)
        directions = [
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1),
            (1, 2),
            (1, -2),
            (-1, 2),
            (-1, -2),
        ]

        visited = set()
        # starting point
        q = deque()
        q.append([0, 0, 0])
        visited.add((0, 0))

        while q:

            row, col, currSteps = q.popleft()

            if row == x and col == y:
                return currSteps

            for dx, dy in directions:

                if (row + dx, col + dy) not in visited:
                    visited.add((row + dx, col + dy))
                    q.append([row + dx, col + dy, currSteps + 1])


print(Solution().minKnightMoves(x=5, y=5))
print(Solution().minKnightMoves(x=2, y=1))
