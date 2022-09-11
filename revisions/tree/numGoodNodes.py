# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.res = 0

        def dfs(root, maxVal):

            # base case is a null node
            if not root:
                return

            # check if good node or not
            if root.val >= maxVal:
                self.res += 1

            maxVal = max(root.val, maxVal)

            dfs(root.left, maxVal)
            dfs(root.right, maxVal)

        dfs(root, root.val)

        return self.res
