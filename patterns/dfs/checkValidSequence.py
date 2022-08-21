# Class of Node
class Node:

    # Constructor to create a
    # node in Binary Tree
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# what did i learn
#


class Solution:
    def isValidSequence(self, root, arr):

        if not root or root.val != arr[0]:
            return False

        def dfs(root, i):
            # if it reach the end of the list then we can return since that is possible height is > than len of sequence
            if not root or i == len(arr):
                return False

            # when we reach a leaf node then we can check for our condition which is if it matches the sequence aka i == last element of the array
            if not root.left or not root.right:
                if root.val == arr[i] and i == len(arr) - 1:
                    return True

            return dfs(root.left, i + 1) or dfs(root.right, i + 1)

        return dfs(root, 0)


arr = [5, 8, 6, 7]
n = len(arr)
root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(2)
root.left.right = Node(4)
root.left.left.left = Node(1)
root.right.left = Node(6)
root.right.left.right = Node(7)

print(Solution().isValidSequence(root, arr))
