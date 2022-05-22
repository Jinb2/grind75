class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        strX = str(x)
        revstrX = strX[::-1]

        return revstrX == strX
