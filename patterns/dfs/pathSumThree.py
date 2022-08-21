# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# revisit
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        self.count = 0
        freq = {0: 1}

        def dfs(root, ps):

            if not root:
                return

            cs = ps + root.val
            x = cs - targetSum

            if x in freq:
                self.count += freq[x]
            if cs in freq:
                freq[cs] += 1
            else:
                freq[cs] = 1

            dfs(root.left, cs)
            dfs(root.right, cs)

            freq[cs] -= 1

        dfs(root, 0)

        return self.count
