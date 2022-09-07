# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # brute force i would store the sum of each nodes in a list
        # and then run through that list and basically create our linekd list from that
        # but we can just do this in one pass
        # adding two numbers regulary is pretty
        # but what if its greater than 10
        # we have a carry
        # keep track of thsi carry and this carry we can get from taking the total and diving by 10
        # since its base 10 20 // 10 = 2
        # 5 + 6 = 11 carry 1 11 // 10 is gonna give us 1
        # 11 mod
        # so we are gonna have two pointers to just iterate throught the numbers

        curr = dummy = ListNode()
        c = 0

        while l1 or l2 or c:

            # lets first initialize our values
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + c

            c = total // 10
            val = total % 10

            curr.next = ListNode(val)
            curr = curr.next

            # move list pointers
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
