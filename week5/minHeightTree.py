class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        # base case
        if n == 1:
            return [0]

        adj = {i: [] for i in range(n)}

        # connect the edges
        for u, v in edges:

            adj[u].append(v)
            adj[v].append(u)

        # all leaf nodes no child nodes only connected to a parent
        leaves = [leaf for leaf in adj if len(adj[leaf]) == 1]

        # we can have two centroid nodes so remove till theres 2 left
        while len(adj) > 2:

            nextLeaves = []

            for leaf in leaves:

                # disconnect from the parent
                parent = adj[leaf].pop()

                # remove this leaf from tree
                del adj[leaf]

                # remove from parent the connection this leaf
                adj[parent].remove(leaf)

                if len(adj[parent]) == 1:
                    nextLeaves.append(parent)

            leaves = nextLeaves

        return leaves
