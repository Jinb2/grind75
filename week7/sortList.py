# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        # merge sort algo
        # get middle of list
        # split into two lists
        # sort two lists
        # merge

        left = head
        right = self.getMid(head)

        # splitting the list
        tmp = right.next
        right.next = None
        right = tmp

        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left, right)

    # get mid
    def getMid(self, head):

        slow = head
        fast = head.next

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, left, right):

        tail = dummy = ListNode()

        while left and right:

            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next

            tail = tail.next

        tail.next = left or right

        return dummy.next
