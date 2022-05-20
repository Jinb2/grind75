# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):

        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val == right.val:

            outPair = self.isMirror(left.left, right.right)
            inPair = self.isMirror(left.right, right.left)

            return outPair and inPair

        return False
