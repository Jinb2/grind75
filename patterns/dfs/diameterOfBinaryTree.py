# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # we can treat a null node as -1 and the reason is as follows
        # the problem defines diameter to be the number of edges beteween two nodes
        # so if we have a leaf node then it will have two out going edges to two nuill nodes
        # so which is why to get the diamaeter we can take the height of the left and right and add 2
        # this will cancel out if they are both null
        # so diameter is height of left and right + 2
        # and then height of a node is left and right + 1 taking the max

        if not root:
            return 0

        res = [0]

        def dfs(root):

            # if root is null then we treat it as -1 conventionally and helps to cancel the edge going out.
            if not root:
                return -1

            left = dfs(root.left)
            right = dfs(root.right)

            # we do +2 because of the number of edges going out
            res[0] = max(2 + left + right, res[0])

            return 1 + max(left, right)

        dfs(root)
        return res[0]
