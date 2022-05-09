# Solution hint: use stack and dict


class Solution:
    def isValid(self, s: str) -> bool:

        currStack = []
        isPar = {"(": ")", "{": "}", "[": "]"}

        for i in range(len(s)):

            if s[i] in isPar:
                currStack.append(s[i])
            else:
                if currStack and s[i] == isPar[currStack[-1]]:
                    currStack.pop()
                else:
                    return False

        return True if not currStack else False
