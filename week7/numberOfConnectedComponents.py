from collections import deque


class Solution:
    def countComponents(self, n, edges):

        # time complexity : O(n + m) n is n and m is len of edges
        # space complexity is gonna be O(m + n) treat edges as m

        # we can have a bfs traversal where we just add start from 0
        # and then after each bfs traversal we add one to number of components
        # we have to check every edge from 0 to n

        # so we start with bfs
        res = 0
        adj = {i: [] for i in range(n)}

        # create our edge
        for u, v in edges:

            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def bfs(edge):

            q = deque()
            q.append(edge)
            visited.add(edge)

            while q:

                # get the edge
                edge = q.popleft()

                # append all the node
                for nei in adj[edge]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)

        for i in range(n):
            if i not in visited:
                bfs(i)
                res += 1
        return res


print(Solution().countComponents(5, [[0, 1], [1, 2], [3, 4]]))
print(Solution().countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))
print(Solution().countComponents(5, [[0, 1], [2, 3], [4, 4]]))
print(Solution().countComponents(6, [[0, 1], [2, 3], [4, 4], [5, 5]]))
