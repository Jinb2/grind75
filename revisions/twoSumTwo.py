class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # O(n^2) run two for loops an dthen check if it equals target
        # however we are given it is sorted so we can use this proeprty
        # two pointsrs to
        # we can use hashmap to sort of store seen numbers O(n) space and runtime
        # increment left and right accordingly depending on if it is smaller or greater than

        l, r = 0, len(numbers) - 1

        while l < len(numbers) and r >= 0:

            twoSum = numbers[l] + numbers[r]

            if twoSum > target:
                r -= 1
            elif twoSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
