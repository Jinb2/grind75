def longest_substring_with_k_distinct(str1, k):

    longestLen = 0
    frequency = {}
    left = 0

    for right in range(len(str1)):

        frequency[str1[right]] = 1 + frequency.get(str1[right], 0)

        while len(frequency) > k:
            frequency[str1[left]] -= 1
            if frequency[str1[left]] == 0:
                del frequency[str1[left]]
            left += 1

        longestLen = max(longestLen, right - left + 1)

    return longestLen


def main():
    print(
        "Length of the longest substr1ing: "
        + str(longest_substring_with_k_distinct("araaci", 2))
    )
    print(
        "Length of the longest substring: "
        + str(longest_substring_with_k_distinct("araaci", 1))
    )
    print(
        "Length of the longest substring: "
        + str(longest_substring_with_k_distinct("cbbebi", 3))
    )


main()
