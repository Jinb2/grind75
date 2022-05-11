# Solution hint: dfs
from typing import *


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:

        rows, cols, orig_color = len(image), len(image[0]), image[sr][sc]

        def dfs(row, col):

            if (
                not (0 <= row < rows and 0 <= col < cols)
                or image[row][col] != orig_color
            ):
                return

            image[row][col] = newColor

            [dfs(row + x, col + y) for (x, y) in ((0, 1), (1, 0), (0, -1), (-1, 0))]

        if orig_color != newColor:
            dfs(sr, sc)

        return image
