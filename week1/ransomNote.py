# Solution hint : use hashmap


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if len(magazine) < len(ransomNote):
            return False

        ransom = {}
        mag = {}

        for i in range(len(ransomNote)):
            ransom[ransomNote[i]] = 1 + ransom.get(ransomNote[i], 0)

        for i in range(len(magazine)):
            mag[magazine[i]] = 1 + mag.get(magazine[i], 0)

        for i in range(len(ransomNote)):

            if (ransomNote[i] not in mag) or (
                ransom[ransomNote[i]] > mag[ransomNote[i]]
            ):
                return False

        return True


solution = Solution()
print("False", solution.canConstruct(ransomNote="a", magazine="b"))
print("False", solution.canConstruct(ransomNote="aa", magazine="ab"))
print("True", solution.canConstruct(ransomNote="aa", magazine="aab"))

# simple one liner
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        return all(ransomNote.count(c) <= magazine.count(c) for c in set(ransomNote))
