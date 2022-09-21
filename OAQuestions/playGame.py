# [1,4,5,5,6]
# [1,3,3,1,5]
# [1, 2, 2, 3, 3, 5]
# [1, 2, 2,2,2,3,3, 3, 3, 5]


def who_wins(nums):
    stack = [-1]
    alice = False
    for num in nums:
        if num == stack[-1]:
            stack.pop()
            alice = not alice
        else:
            stack.append(num)

    return "Alice" if alice else "Bob"


print(who_wins([1, 4, 5, 5, 6]))
print(who_wins([1, 3, 3, 1, 5]))
print(who_wins([1, 2, 2, 3, 3, 5]))
