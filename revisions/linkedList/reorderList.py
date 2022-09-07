# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # what is goal
        # pattern
        # we are following this pattern
        # we are splitting the linked list and append from first then append from second and rrepeat
        # so we want to first get the middle of the list and reverse
        # from there we can just iterate through using a dummy node and return the dummy.next

        # first i want to get the middle
        slow, fast = head, head.next

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        # so slow is going to be the first half we want the second half
        # we also want to break it off before we reverse
        temp = slow.next
        slow.next = None
        slow = temp

        first, second = head, slow

        # initialize prev to none
        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # now prev is going to be at the head of the reversed
        second = prev

        # since second is smaller we just stop when it runs out
        while second:

            # store the pointers for the next node
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
