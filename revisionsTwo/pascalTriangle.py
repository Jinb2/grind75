class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        # initially starts at 1
        # n is len of row
        # this is O(n^2) since need to traverse n rows and then length of n
        res = [[1]]

        for i in range(numRows - 1):

            # temp to let us add
            # use 0 for numbers at edge
            temp = [0] + res[-1] + [0]
            row = []
            # each number add top left and right

            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            res.append(row)

        return res
