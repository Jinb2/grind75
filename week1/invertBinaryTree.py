# Solution hint : pointer
from typing import *


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root:
            # swap the children
            tmp = root.left
            root.left = root.right
            root.right = tmp

            # recursively call on the left and right
            self.invertTree(root.left)
            self.invertTree(root.right)

            return root
        else:
            return None
