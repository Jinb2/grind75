# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # at every node we want to want to swap its children
        # O(n) time nd space since we will need to visit at worst evety node
        # our base case is a null node wich we can just return

        if not root:
            return

        # swap so we need to store temp var
        temp = root.left
        root.left = root.right
        root.right = temp

        # now we recursively clal on the left and right

        self.invertTree(root.left)
        self.invertTree(root.right)

        # finally return up root
        return root
