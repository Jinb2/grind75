class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = [0]

        def dfs(root):

            if not root:
                return -1

            left = dfs(root.left)
            right = dfs(root.right)

            res[0] = max(left + right + 2, res[0])

            return 1 + max(left, right)

        dfs(root)
        return res[0]
