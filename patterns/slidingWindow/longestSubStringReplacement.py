"""
Problem Statement 
Given a string with lowercase letters only, if you are allowed to replace no more than k letters with any letter, find the length of the longest substring having the same letters after replacement.
Example 1:
Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
Example 2:
Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
Example 3:
Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
"""


def length_of_longest_substring(str1, k):

    freq = {}
    maxLength, left, max_repeat_count = 0, 0, 0

    for right in range(len(str1)):

        freq[str1[right]] = 1 + freq.get(str1[right], 0)

        max_repeat_count = max(max_repeat_count, freq[str1[right]])

        if (right - left + 1 - max_repeat_count) > k:

            freq[str1[left]] -= 1
            left += 1

        maxLength = max(maxLength, right - left + 1)

    return maxLength


print(length_of_longest_substring("aabccbb", 2))
print(length_of_longest_substring("abbcb", 1))
print(length_of_longest_substring("abccde", 1))
