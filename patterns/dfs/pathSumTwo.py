# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        # helper function
        # node currSum currPath
        # base cases
        # if the node exists check if its a leaf and then check if it equals targetsum
        # after that we can pop
        # if not then return and pop
        # recursively check

        if not root:
            return []

        res = []

        def dfs(root, currSum, currPath):

            if not root:
                return None

            currSum += root.val
            currPath.append(root.val)

            # check if its a child currSum ==
            if not root.left and not root.right and currSum == targetSum:
                res.append(currPath[::])
            else:
                # recursively call on left and right
                dfs(root.left, currSum, currPath)
                dfs(root.right, currSum, currPath)

            currPath.pop()

        dfs(root, 0, [])

        return res
