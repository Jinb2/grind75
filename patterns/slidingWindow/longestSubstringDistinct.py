"""
Problem Statement 
Given a string, find the length of the longest substring which has no repeating characters.
Example 1:
Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".
Example 2:
Input: String="abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".
Example 3:
Input: String="abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".
"""


def non_repeat_substring(s):

    maxLength, left, = (
        0,
        0,
    )

    freq = {}

    for right in range(len(s)):

        freq[s[right]] = 1 + freq.get(s[right], 0)

        while freq[s[right]] > 1:

            freq[s[left]] -= 1
            left += 1

        maxLength = max(maxLength, right - left + 1)

    return maxLength


print(non_repeat_substring("aabccbb"))
print(non_repeat_substring("abbbb"))
print(non_repeat_substring("abccde"))
