class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # bruteforce is O(mn) search every element
        # but instead we know that every element is sorted in the matrix
        # each row is always larger than the prev row
        
        rows,cols = len(matrix), len(matrix[0])

        # lets find the row the number could be on
        top,bot = 0, rows - 1

        while top <= bot:

            # check if in range
            row = (top+bot) // 2

            # we found the row
            if target < matrix[row][0]:
                bot = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                # we found the value
                break
        
        # the number could not even exist in any of the rows
        # we know if it exists if top <= bottom
        if not (top <= bot):
            return False

        row = (top+bot) // 2

        # now binary search on the row
        search = matrix[row]

        l,r = 0, len(search) - 1

        while l <= r:

            mid = (l+r) // 2

            if search[mid] == target:
                return True
            elif search[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False


        



        