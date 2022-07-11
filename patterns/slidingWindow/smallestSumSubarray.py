import math


def smallest_subarray_sum(s, arr):

    windowSum = 0
    left = 0

    smallestLen = math.inf

    for right in range(len(arr)):

        windowSum += arr[right]

        while windowSum >= s:
            smallestLen = min(smallestLen, right - left + 1)
            windowSum -= arr[left]
            left += 1

    if smallestLen == math.inf:
        return 0

    return smallestLen


def main():
    print(
        "Smallest subarray length: " + str(smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2]))
    )
    print("Smallest subarray length: " + str(smallest_subarray_sum(8, [3, 4, 1, 1, 6])))
    print(
        "Smallest subarray length: " + str(smallest_subarray_sum(8, [2, 1, 5, 2, 3, 2]))
    )


main()
