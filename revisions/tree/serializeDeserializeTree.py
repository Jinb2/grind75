# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    # root left right
    # preorder traversal
    # how should we deal with null nodes ? => mark it as "N"
    # store the output as a list initallly
    # we seperate by a ","

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def preorder(root):

            if not root:
                res.append("N")
                return

            # root
            res.append(str(root.val))
            # left
            preorder(root.left)
            # right
            preorder(root.right)

        preorder(root)
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        # we are given a string so using our example
        # "12NN34NN5NN"
        # data is a string lets turn into a list
        nodes = data.split(",")
        self.i = 0

        def dfs():

            # root left right
            # base case
            if nodes[self.i] == "N":
                self.i += 1
                return None

            root = TreeNode(int(nodes[self.i]))
            # now need to go to next node
            self.i += 1
            root.left = dfs()
            root.right = dfs()

            return root

        return dfs()
