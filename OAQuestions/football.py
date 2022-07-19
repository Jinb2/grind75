# https://leetcode.com/discuss/interview-question/1930478/football-scores-hackerrank-question
def foot(teamA, teamB):

    # sort team A
    teamA.sort()
    res = []

    for numB in teamB:

        l, r = 0, len(teamA) - 1

        while l <= r:

            mid = (l + r) // 2

            if teamA[mid] > numB:
                r = mid - 1
            else:
                l = mid + 1

        res.append(l)

    return res


print(foot([2, 10, 5, 4, 8], [3, 1, 7, 8]))
