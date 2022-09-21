def solution(nums):

    maxNum = max(nums) * 2
    perfectSq = set()

    count = 0
    for i in range(maxNum):

        square = i**2

        if square > maxNum:
            break

        perfectSq.add(square)

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            sum = nums[i] + nums[j]

            if sum >= 0 and sum in perfectSq:
                print(i, j)
                count += 1

    return count


print(solution([-1, 18, 3, 1, 5]))
