"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


# how did i do this problem
# I did it using dfs because we need to go to each "old" node and then creating a copy
# so we store this mapping in a hashmap
# so essentially we have it that we can check if we created a copy
# so how our algo works is that
# we have the base case where it is already created in that case we can return the copy node
# so then we iterate through the neighbors and call dfs
# appending it once we reach a base case


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":

        if not node:
            return node
        # creating our graph
        # old to new nodes

        # create that node
        # apepnd the neighbors and then return

        oldToNew = {}

        def dfs(node):

            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)
