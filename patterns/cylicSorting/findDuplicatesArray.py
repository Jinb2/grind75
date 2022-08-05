class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        # mark the seen numbers with negative
        res = []

        for num in nums:

            num = abs(num)

            # if we visit it and its negative that means weve seen it before so its a dupe
            if nums[num - 1] < 0:
                res.append(num)
            else:
                nums[num - 1] = nums[num - 1] * -1

        return res
