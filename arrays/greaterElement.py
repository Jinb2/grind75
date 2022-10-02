class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # montonoically decreasing stack
        # only add to stack if exists in nums1
        idx = {n: i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)

        stack = []

        for num in nums2:

            while stack and num > stack[-1]:

                val = stack.pop()
                i = idx[val]
                res[i] = num

            if num in idx:
                stack.append(num)

        return res
