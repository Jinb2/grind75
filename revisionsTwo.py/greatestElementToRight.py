class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        # brute force is to O(n^2) going through array twic
        # right what coms to mind is to just iterate through array nd then just replace iwth ele

        # case of length 1
        if len(arr) == 1:
            return [-1]

        # start athe back and then keep track of largest num seen so far
        prev = arr[-1]

        for i in range(len(arr) - 2, -1, -1):

            newMax = max(prev, arr[i])
            arr[i] = prev
            prev = newMax

        arr[-1] = -1

        return arr
