class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visitSet = set()  # course in our dfs path

        def dfs(crs):

            if crs in visitSet:
                return False

            # no prereq
            if preMap[crs] == []:
                return True

            visitSet.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            visitSet.remove(crs)
            preMap[crs] = []

            return True

        # just call on each course number
        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True
