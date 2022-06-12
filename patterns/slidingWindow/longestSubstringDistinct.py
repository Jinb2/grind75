from cmath import e


def longest_substring_with_k_distinct(str1, k):

    longestSub = 0
    l = 0
    seenChars = {}

    for i in range(len(str1)):

        if str1[i] not in seenChars:
            seenChars[str1[i]] = 1
        else:
            seenChars[str1[i]] += 1

        while len(seenChars) > k:

            seenChars[str1[l]] -= 1
            if seenChars[str1[l]] == 0:
                del seenChars[str1[l]]
            l += 1

        longestSub = max(longestSub, i - l + 1)

    return longestSub


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
