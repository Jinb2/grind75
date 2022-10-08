class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):

        res = ""

        for s in strs:

            res += str(len(s)) + "#" + s

        return res

    def decode(self, str):

        res, i = [], 0

        while i < len(str):

            j = i
            # 3#code
            while str[j] != "#":
                j += 1

            length = int(str[i:j])
            res.append(str[j + 1 : j + length + 1])

            i = j + length + 1

        return res
