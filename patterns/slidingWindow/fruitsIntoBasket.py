"""
Problem Statement 
Given an array of characters where each character represents a fruit tree, you are given two baskets and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.
You can start with any tree, but once you have started you cant skip a tree. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
Write a function to return the maximum number of fruits in both the baskets.
Example 1:
Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
Example 2:
Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
"""


def fruit_into_baskets(fruits):

    fruitFreq = {}
    left = 0
    maxFruit = 0

    for i in range(len(fruits)):

        fruitFreq[fruits[i]] = 1 + fruitFreq.get(fruits[i], 0)

        while len(fruitFreq) > 2:

            fruitFreq[fruits[left]] -= 1
            if fruitFreq[fruits[left]] == 0:
                del fruitFreq[fruits[left]]

            left += 1

        maxFruit = max(maxFruit, i - left + 1)

    return maxFruit


print(fruit_into_baskets(["A", "B", "C", "A", "C"]))
print(fruit_into_baskets(["A", "B", "C", "B", "B", "C"]))
