# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        res = [root.val]

        def dfs(root):

            if not root:
                return 0

            # we are not splitting
            # we take the path with the greatest sum
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)

            # we could have negative numbers so if its negative we can make it 0
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # compute max with split from this root
            res[0] = max(root.val + leftMax + rightMax, res[0])

            # so we return to the parent the value of without splitting
            return root.val + max(leftMax, rightMax)

        dfs(root)

        return res[0]
