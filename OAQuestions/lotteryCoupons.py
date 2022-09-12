# https://www.chegg.com/homework-help/questions-and-answers/lottery-n-coupons-n-people-take-part--person-picks-exactly-one-coupon-coupons-numbered-con-q100150573
def lotteryCoupons(n):

    # store the sum and count of winners
    winners = {}

    for i in range(n + 1):

        sum = 0
        while i:
            sum += i % 10
            i //= 10

        winners[sum] = 1 + winners.get(sum, 0)

    maxWinners = max(winners, key=winners.get)  # count
    res = 0

    maxCount = winners[maxWinners]

    for sum, count in winners.items():

        if count == maxCount:
            res += 1

    return res


print(lotteryCoupons(12))
