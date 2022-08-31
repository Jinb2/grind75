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

        res,i = [],0

        while i < len(str):

            # where delimeter starts
            j = i
            # 10#hensotlao93#len
            while str[j] != "#":
                j += 1
            
            # how long string is
            length = int(str[i:j])
            res.append(str[j+1:j+1+length])
            # where the next string begins
            i = j + 1 + length

        return res