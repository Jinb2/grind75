class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return root

        res = []
        q = deque()
        q.append(root)

        leftToRight = True

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

                if leftToRight:
                    res.append(level)
                else:
                    res.append(level[::-1])

            # switch the direction
            leftToRight = not leftToRight

        return res
