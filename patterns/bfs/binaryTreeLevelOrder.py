# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return root

        # initialize a queue
        # append the root
        # init a res var
        # while queue is not empty
        # store list for the nodes at this current level
        # go through nodes in level -> for loop
        # if node is null then we need to ignore it
        # append its left and right children
        # append list if not empty
        # return

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

        return res
