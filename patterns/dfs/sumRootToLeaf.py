# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        """
        dfs approach
        initialize a result var that keeps track of total sum

        helper function
        node and then currNum as a string


        base case is none and then leaf node

        for none we just retur and for leaf we will convert it to a integer and then add it to our global sum
        """

        res = [0]

        def dfs(root, currPath):

            if not root:
                return

            currPath += str(root.val)

            # check if its a leaf node
            if not root.left and not root.right:
                currVal = res[0]
                res[0] = currVal + int(currPath)

            dfs(root.left, currPath)
            dfs(root.right, currPath)

        dfs(root, "")

        return res[0]
