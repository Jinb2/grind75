# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or k == 0:
            return head

        # first get the length of the linked list
        ptr = head
        length = 0

        while ptr:

            length += 1
            ptr = ptr.next

        if k % length or k % length == 0:
            return head
        # get the place to where we need to separate the linked list

        firstHalf = head

        n = length - (k % length) if k > length else length - k

        for _ in range(n - 1):
            firstHalf = firstHalf.next

        # split this linked list
        secondHalf = firstHalf.next
        firstHalf.next = None

        # get to end of list from second half
        end = secondHalf

        while end and end.next:
            end = end.next

        end.next = head

        return secondHalf
