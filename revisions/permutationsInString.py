class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        # a variation of anagrams
        countS1, countS2 = [0] * 26,[0] * 26

        for i in range(len(s1)):
            countS1[ord(s1[i]) - ord("a") ] += 1
            countS2[ord(s2[i]) - ord("a")] += 1
        
        matches = 0

        for i in range(26):
            if countS1[i] == countS2[i]:
                matches += 1
        
        l = 0

        for r in range(len(s1),len(s2)):

            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            countS2[index] += 1

            if countS2[index] == countS1[index]:
                matches += 1
                # s2 count is bigger
            elif countS1[index] + 1 == countS2[index]:
                matches -= 1

            index = ord(s2[l]) - ord("a")
            countS2[index] -= 1

            if countS2[index] == countS1[index]:
                matches += 1
            # s2 count is smaller
            elif countS1[index] - 1 == countS2[index] :
                matches -= 1
            
            l += 1
        
        return matches == 26