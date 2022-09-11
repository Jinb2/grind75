# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # binary search tree
        # all elements to left of root is less and right is greater
        # so using this fact we can see that there is some sort of boundary for each node
        # and then check that it meets these boundaries
        # O(n) since we need to check every node
        # do this bfs way
        # edge case is if root is null in that case return true

        if not root:
            return True

        def dfs(root, left, right):

            # base case
            if not root:
                return True

            if left < root.val < right:
                # search left and right
                return dfs(root.left, left, root.val) and dfs(
                    root.right, root.val, right
                )
            else:
                return False

        return dfs(root, float("-infinity"), float("infinity"))
