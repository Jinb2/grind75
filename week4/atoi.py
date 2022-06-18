class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.strip()
        res = ""

        for c in s:
            if not res and (c in ["-", "+"]):
                res += c
            elif c.isdigit():
                res += c
            else:
                break

        if res and res not in ["-", "+"]:

            if int(res) > 0:
                return min(2**31 - 1, int(res))
            else:
                return max(-(2**31), int(res))

        return 0
