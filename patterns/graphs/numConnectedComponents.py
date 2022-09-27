class Solution:
    def numConnected(n, edges):

        graph = {i: [] for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node):

            if node in visited:
                return

            visited.add(node)

            # traverse its neighbors
            for edge in graph[node]:
                dfs(edge)

        res = 0
        for i in range(n):

            if i not in visited:
                dfs(i)
                res += 1
        return res


print(Solution.numConnected(5, [[0, 1], [1, 2], [3, 4]]))
print(Solution.numConnected(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))
