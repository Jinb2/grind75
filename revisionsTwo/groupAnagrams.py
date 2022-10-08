class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # words that are anagrams have same char count
        # get the count of each words char
        # hashmap [count] : [words]
        # use ord value of a character to get the index and to store count

        anagrams = defaultdict(list)

        for s in strs:

            countS = [0] * 26
            for c in s:

                countS[ord(c) - ord("a")] += 1

            anagrams[tuple(countS)].append(s)

        return [anagram for _, anagram in anagrams.items()]
