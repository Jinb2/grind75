# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # we can do this question in two ways
        # bfs or dfs
        # both will take us O(n) space and time

        # for dfs we can take the base case as being a null root
        # null roots should not count towards height so we will count it to have a height of 1
        # we will recursively call left and right adding 1 to the max of the left or right

        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def bfs(self, root: Optional[TreeNode]) -> int:

        # for bfs we can just traverse level and once we finish a level we incremetn
        # depth use stack for this

        if not root:
            return 0

        q = deque()
        q.append(root)
        res = 0

        while q:

            qLen = len(q)

            for _ in range(qLen):

                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res += 1

        return res
