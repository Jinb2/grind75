# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        res = [0]

        def dfs(root):

            # if root is null then we treat it as -1 conventionally and helps to cancel the edge going out.
            if not root:
                return -1

            left = dfs(root.left)
            right = dfs(root.right)

            # we do +2 because of the number of edges going out
            res[0] = max(2 + left + right, res[0])

            return 1 + max(left, right)

        dfs(root)
        return res[0]
