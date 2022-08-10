# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return root

        q = deque()
        q.append(root)

        res = []

        q = deque()
        q.append(root)
        res = []

        while q:

            qLen = len(q)
            level = []

            for _ in range(qLen):

                node = q.popleft()

                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                res.append(level)

        return res[::-1]
