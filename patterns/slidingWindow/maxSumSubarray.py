# sliding window technique


def max_sub_array_of_size_k(k, arr):
    # TODO: Write your code here

    maxSum, windowSum = 0, 0
    start = 0

    for end in range(len(arr)):

        windowSum += arr[end]

        if end >= k - 1:
            maxSum = max(maxSum, windowSum)
            windowSum -= arr[start]
            start += 1

    return maxSum


def main():
    print(
        "Maximum sum of a subarray of size K: "
        + str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2]))
    )
    print(
        "Maximum sum of a subarray of size K: "
        + str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5]))
    )


main()
