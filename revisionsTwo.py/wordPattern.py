class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        patMap = {}
        sMap = {}

        words = s.split()

        if len(words) != len(pattern):
            return False

        for i in range(len(pattern)):

            c = pattern[i]
            word = words[i]

            if c in patMap and patMap[c] != word:
                return False

            if word in sMap and sMap[word] != c:
                return False

            patMap[c] = word
            sMap[word] = c

        return True
