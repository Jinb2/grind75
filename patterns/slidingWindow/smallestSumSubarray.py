def smallest_subarray_sum(s, arr):

    smallestSum, currSum = float("inf"), 0
    start = 0

    for end in range(len(arr)):

        currSum += arr[end]

        if currSum > s:
            currSum -= arr[start]
            start += 1

        if currSum == s:
            smallestSum = min(smallestSum, end - start + 1)

    return smallestSum


def main():
    print(
        "Smallest subarray length: " + str(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2]))
    )
    print("Smallest subarray length: " + str(smallest_subarray_sum(8, [3, 4, 1, 1, 6])))
    print(
        "Smallest subarray length: " + str(smallest_subarray_sum(8, [2, 1, 5, 2, 3, 2]))
    )


main()
