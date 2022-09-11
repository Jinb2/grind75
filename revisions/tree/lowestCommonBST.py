# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        curr = root
        # O(logn) n is the number of nodes since this is a BST we know whether to traverse left or right
        while curr:

            # check if curr is either p or q so that means its a desecendant
            if curr == p or curr == q:
                return curr

            # curr is too big
            if curr.val > p.val and curr.val > q.val:
                curr = curr.left
            elif curr.val < p.val and curr.val < q.val:
                curr = curr.right
            else:
                return curr
