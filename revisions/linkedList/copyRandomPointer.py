"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":

        # lets use a hashmap and store copies of the nodes with respect to old
        # O(n) space and runtime
        # we also need to consider if a node points to a a null node
        # so that will be one of our edge cases
        oldToCopy = {None: None}

        # run through and create the copies
        curr = head

        while curr:
            oldToCopy[curr] = Node(curr.val)  # create copy
            curr = curr.next

        # run through again and we want to start connecting
        curr = head

        while curr:

            # we need to connect to its next
            # and to its random
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next

        return oldToCopy[head]
