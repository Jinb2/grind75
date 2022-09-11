# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # the diameter can be calulated by taking height of left and right tree + 2
        # we add to account for the two edges going out
        # because of this we want to return up the heights at each node
        # the height of each node is found by taking the max of the left and right
        # a null node will contribute negative 1 to the diameter
        self.res = 0

        def dfs(root):

            if not root:
                return -1

            # calculate height of left and right
            left = dfs(root.left)
            right = dfs(root.right)

            self.res = max(self.res, left + right + 2)

            # treat a leaf node as having height of 0
            return 1 + max(left, right)

        dfs(root)

        return self.res
