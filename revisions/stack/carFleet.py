class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = [(p, s) for p, s in zip(position, speed)]

        # contains the number of fleets
        stack = []

        # because last positon always will have same speed no matter what
        # since it has nothing coming after it so cars before have to match its speed
        for p, s in sorted(pair)[::-1]:

            time = (target - p) / s
            stack.append(time)

            # this means the recently added car to stack will finish at the same time
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
