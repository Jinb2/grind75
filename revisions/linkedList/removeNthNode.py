# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # brute force is we caclulat ethe length of list and then subtract it by n
        # this will give us the nth position
        # how ever you notice that nth node is going to be size n from the end
        # sso we can have a fast pointer that iterates by n times and then
        # we have a slow pointer and we keeep iterating till the fast pointer reaches end of list

        # what if we remove the first node
        # we can accoutn for this edge case by using a dummy node
        prev = dummy = ListNode(0, head)

        slow, fast = head, head
        # move fast pointer till its
        for _ in range(n):
            fast = fast.next

        # slow will be at the nth node
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next

        # now lets just remove
        prev.next = slow.next
        slow.next = None

        return dummy.next
