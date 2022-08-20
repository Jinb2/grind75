class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:

        # base case is if the orig color is not eq to new color
        # other wise we are gonna run dfs

        # dfs function is gonna tkae in the row and col
        # change the color
        # check if the new coord is equal to the orig color
        # if it is then we can run dfs on that row col

        # return the grid

        rows, cols = len(image), len(image[0])

        def dfs(r, c):

            # change the color
            image[r][c] = newColor

            directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]

            for x, y in directions:
                row, col = r + x, c + y
                if (
                    (row in range(rows))
                    and (col in range(cols))
                    and (image[row][col] == origColor)
                ):
                    dfs(row, col)

        # if orig color equals new color then we return the same grid
        # orig color at the starting point
        origColor = image[sr][sc]
        newColor = color

        if origColor != newColor:
            dfs(sr, sc)

        return image
