# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # if not head or k == 0:
        #     return head

        # # first get the length of the linked list
        # ptr = head
        # length = 0

        # while ptr:

        #     length += 1
        #     ptr = ptr.next

        # if k % length or k % length == 0:
        #     return head
        # # get the place to where we need to separate the linked list

        # firstHalf = head

        # n = length - (k % length) if k > length else length - k

        # for _ in range(n - 1):
        #     firstHalf = firstHalf.next

        # # split this linked list
        # secondHalf = firstHalf.next
        # firstHalf.next = None

        # # get to end of list from second half
        # end = secondHalf

        # while end and end.next:
        #     end = end.next

        # end.next = head

        # return secondHalf

        # cleaner code

        if not head:
            return head

        length, tail = 1, head

        while tail.next:

            length += 1
            tail = tail.next

        k = k % length

        if k == 0:
            return head

        curr = head

        for _ in range(length - k - 1):

            curr = curr.next

        newHead = curr.next
        curr.next = None

        tail.next = head

        return newHead
