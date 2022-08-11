# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        q = deque()
        q.append([root, 1])

        while q:

            node, depth = q.popleft()

            if node:
                # reached leaf node then we can just return right away since this is BFS
                if not node.left and not node.right:
                    return depth
                else:
                    q.append([node.left, depth + 1])
                    q.append([node.right, depth + 1])
