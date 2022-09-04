class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []
        q = deque()

        l,r = 0,0

        # queue first value alwayhs gonna be the largest
        while r < len(nums):
            
            # get the top value from index
            while q and nums[r] > nums[q[-1]]:
                q.pop()

            # append the index at which the number is founds
            q.append(r)  

            # we need to check if the largest value is removed or not
            if l > q[0]:
                q.popleft()
            
            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1

            r += 1

        return res