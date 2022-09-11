# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # preorder is
        # root left right
        # inorder is left root right
        # so every first element in the preorder is root
        # we can find its left and right subtree from inorder
        # specifically find the index at which this root appears inorder
        # all elements left to this index are the left subtree and vice versa right  subtree
        # base case is if we run out of either preorder or inorder we cna return none since that menas we reached
        # left nodes children

        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])

        return root
