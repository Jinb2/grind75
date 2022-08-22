class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # stack solution
        # negative asteroid wont ever collide if asteroid on left is negative
        # three cases
        # case 1 is negative and no positive then we can just push
        # case 2 is same direction
        # case three is positeve nad thne negative then its gonna collide
        # keep track of all the asteroids
        res = []

        for asteroid in asteroids:

            # collision only occurs when we add a negative to top of positive stack
            while res and asteroid < 0 and res[-1] > 0:

                # same size so both are destroyed
                if res[-1] == abs(asteroid):
                    res.pop()
                    break

                # dont append yet because there could be more potential positive collisions
                elif res[-1] < abs(asteroid):
                    res.pop()
                    continue
                else:
                    break
            else:
                res.append(asteroid)

        return res
