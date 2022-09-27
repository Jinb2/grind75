from typing import (
    List,
)

from collections import deque


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here
        if n - 1 != len(edges):
            return False

        graph = {i: [] for i in range(n)}
        visited = set()

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        q = deque()
        q.append(0)
        visited.add(0)

        while q:

            node = q.popleft()
            print("Visiting", node)
            for edge in graph[node]:
                if edge not in visited:
                    q.append(edge)
                    visited.add(edge)

        # there can be disjoint
        return len(visited) == n


print(Solution().valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))


#####################
# DFS
#####################
from typing import (
    List,
)

from collections import deque


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # write your code here
        if n - 1 != len(edges):
            return False

        graph = {i: [] for i in range(n)}
        visited = set()

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # prev is to prevent false loop detection
        def dfs(i, prev):

            if i in visited:
                return False

            visited.add(i)

            for edge in graph[i]:

                # if the edge is the previous edge we came from
                if edge == prev:
                    continue

                if not dfs(edge, i):
                    return False

            return True

        # there could be disjoint
        return dfs(0, -1) and n == len(visited)
