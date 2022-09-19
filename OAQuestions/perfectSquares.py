def perfectSquares(nums):

    res = 0
    maxSum = getMax(nums)
    perfectSquares = getPerfectSquares(maxSum)

    for i in range(len(nums)):

        res += getPairs(nums[i], perfectSquares, nums)

    return res


def getPairs(n, perfectSquares, nums):

    count = 0

    if n + n in perfectSquares:
        count += 1

    for num in perfectSquares:

        target = num - n

        if target > n and target in nums:
            count += 1

    return count


def getMax(nums):

    firstMax = 0
    secondMax = 0

    if nums[0] > nums[1]:
        firstMax = nums[0]
        secondMax = nums[1]
    else:
        firstMax = nums[1]
        secondMax = nums[0]

    for i in range(2, len(nums)):

        if nums[i] > firstMax:
            secondMax = firstMax
            firstMax = nums[i]
        elif nums[i] > secondMax:
            secondMax = nums[i]

    return firstMax + secondMax


def getPerfectSquares(n):

    perfectSquares = set()
    curr = 1
    i = 1

    while curr <= n:
        perfectSquares.add(curr)
        i += 1
        curr = i**2

    return perfectSquares


print(perfectSquares([1, 2, 3, 4]))
print(perfectSquares([1, 2, 3, 4, 5]))
