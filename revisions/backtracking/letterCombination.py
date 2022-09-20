class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        # create hashmap of digit to char
        digitsToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []

        def backtrack(i, curr):

            # what is condition for a solution
            if len(curr) == len(digits):
                res.append(curr)
                return

            # out of bounds
            if i > len(digits):
                return

            for c in digitsToChar[digits[i]]:
                # append all possible combinations
                backtrack(i + 1, curr + c)

        backtrack(0, "")

        return res
