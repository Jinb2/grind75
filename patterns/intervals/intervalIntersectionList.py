class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:

        # pointer for first and second list
        i, j = 0, 0

        res = []

        while i < len(firstList) and j < len(secondList):

            aStart, aEnd = firstList[i]
            bStart, bEnd = secondList[j]

            if aStart <= bEnd and bStart <= aEnd:
                res.append([max(aStart, bStart), min(aEnd, bEnd)])

            if aEnd <= bEnd:
                i += 1
            else:
                j += 1

        return res
