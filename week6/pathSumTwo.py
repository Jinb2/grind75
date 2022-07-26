# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        res = []

        def dfs(root, targetSum, path):

            if root == None:
                return []

            targetSum -= root.val

            path.append(root.val)

            if not root.left and not root.right:  # leafnode

                if targetSum == 0:
                    res.append(path[::])
            else:

                dfs(root.left, targetSum, path)
                dfs(root.right, targetSum, path)

            path.pop()

        dfs(root, targetSum, [])

        return res
