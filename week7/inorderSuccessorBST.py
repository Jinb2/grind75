class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """

    def inorderSuccessor(self, root, p):
        # write your code here

        successor = None

        while root:

            if p.val >= root.val:
                root = root.right
            else:
                successor = root
                root = root.left

        return successor
