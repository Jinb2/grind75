# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # balanced tree means height diffs by no more than 1 and also both left and right subtrees contain
        # balanced trees
        # so we can recursively calculate left and right heights and also store whether it is balanced

        def dfs(root):

            # null nodes are balanced and have height of 0
            if not root:
                return [True, 0]

            # other wise calculate height of left and right
            left = dfs(root.left)
            right = dfs(root.right)

            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
