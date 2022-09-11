# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # is we are gonna take sum of splitting and without
        self.res = root.val

        def dfs(root):

            # pass up the height
            if not root:
                return 0

            # lets compute sum splitting
            left = dfs(root.left)
            right = dfs(root.right)
            leftMax = max(left, 0)
            rightMax = max(right, 0)

            self.res = max(self.res, leftMax + rightMax + root.val)
            # return without splitting
            return root.val + max(leftMax, rightMax)

        dfs(root)

        return self.res
