class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        """
        binary tree follows pattern of
        left child has index 2*i + 1 right has index 2*i + 2
        """

        queue = deque()
        queue.append([root, 0])

        maxWidth = 1

        while queue:

            start = queue[0][1]
            end = queue[-1][1]

            maxWidth = max(maxWidth, end - start + 1)

            for _ in range(len(queue)):
                curr, idx = queue.popleft()

                if curr.left:
                    queue.append([curr.left, 2 * idx + 1])
                if curr.right:
                    queue.append([curr.right, 2 * idx + 2])

        return maxWidth
