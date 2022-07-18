class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        wordFreq = Counter(words)
        wordLen = len(words[0])
        numWords = len(words)
        totalLen = numWords * wordLen

        res = []

        for i in xrange(wordLen):

            left = i
            seenStr = defaultdict(int)
            count = 0

            for j in range(i, len(s) - wordLen + 1, wordLen):

                word = s[j : j + wordLen]

                if word in wordFreq:

                    seenStr[word] += 1
                    count += 1

                    while seenStr[word] > wordFreq[word]:

                        seenStr[s[left : left + wordLen]] -= 1
                        left += wordLen
                        count -= 1

                    if count == numWords:
                        res.append(left)
                else:

                    left = j + wordLen
                    seenStr = defaultdict(int)
                    count = 0

        return res
