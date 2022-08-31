class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # O(nm)  runtime
        # O(26n) space
        # we going to use hashmap and store by the count of the words
        anagrams = defaultdict(list)

        # now iterate through each word and store count
        for s in strs:

            count = [0] * 26

            # we can get the value by subtracting from a
            for c in s:
                count[ord(c) - ord("a")] += 1

            anagrams[tuple(count)].append(s)

        return anagrams.values()
