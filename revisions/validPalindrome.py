class Solution:
    def isPalindrome(self, s: str) -> bool:

        # we cna use two pointers O(n)
        # one starting from beginning and one start from end
        # we skip any non alpha nums
        # compare the two pointers changing it to lowercase and if its equal increment
        # if not return False

        l, r = 0, len(s) - 1

        while l < r:

            # first move pointers while theyre not alanum
            while l < r and not self.isalnum(s[l]):
                l += 1

            while l < r and not self.isalnum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True

    def isalnum(self, c):

        return (
            (ord("0") <= ord(c) <= ord("9"))
            or (ord("A") <= ord(c) <= ord("Z"))
            or (ord("a") <= ord(c) <= ord("z"))
        )
