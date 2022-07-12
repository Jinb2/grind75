class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # build adjaceny list of prereqs

        prereq = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        # course has 3 possible states

        # visited -> added to output
        # visiting -> crs not in output but is in cycle
        # unvisited -> not added to output or cycle

        output = []
        visit, cycle = set(), set()

        def dfs(crs):

            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False

            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return output
