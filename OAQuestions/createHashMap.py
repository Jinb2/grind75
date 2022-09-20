# O(1) sol
def solution(queryType, query):
    ans = 0
    hmap = {}
    # culmative sum of key and val
    ck = 0
    cv = 0

    # they maintain the offset of the vals

    for i in range(len(queryType)):

        # the command
        cmd = queryType[i]
        # the input
        quer = query[i]

        if cmd == "insert":
            key, val = quer[0], quer[1]
            hmap[key - ck] = val - cv
        elif cmd == "addToValue":
            k = quer[0]
            cv += k
        elif cmd == "addToKey":
            k = quer[0]
            ck += k
        else:
            k = quer[0]
            k -= ck

            val = hmap[k] + cv

            ans = ans + val

    return ans


solution(
    ["insert", "addToValue", "get", "insert", "addToKey", "addToValue", "get"],
    [[1, 2], [2], [1], [2, 3], [1], [-1], [3]],
)
