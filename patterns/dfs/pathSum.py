class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        # root.val if curr path is viable should equal target sum
        if not root.left and not root.right and root.val == targetSum:
            return True

        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(
            root.right, targetSum - root.val
        )

        # with helper
        # def dfs(node, currSum):

        #     if not node:
        #         return False

        #     currSum += node.val

        #     if not node.left and not node.right:
        #         return currSum == targetSum

        #     return dfs(node.left, currSum) or dfs(node.right, currSum)

        # return dfs(root, 0)
