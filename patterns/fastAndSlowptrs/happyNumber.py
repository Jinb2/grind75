class Solution:
    def isHappy(self, n: int) -> bool:

        slow = self.squared(n)
        fast = self.squared(self.squared(n))

        while slow != fast and fast != 1:

            slow = self.squared(slow)
            fast = self.squared(self.squared(fast))

        return fast == 1

    def squared(self, n):

        output = 0

        while n:

            digit = n % 10  # last digit
            output += digit**2
            n = n // 10  # get next digit

        return output
