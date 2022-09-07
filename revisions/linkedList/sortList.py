# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # want to sort list
        # any sorting algorithims? => merge sort O(nlogn)
        # idea is we break apart list everytime and sort and merge
        # what is our stopping condition
        # when there exists only one item left or if the node is null

        # lets write our base case
        if not head or not head.next:
            return head

        # first we need to figure out the first and second portion
        first = head
        # our function returns the last element in the first half so we need the second half
        second = self.getMid(head)

        # we need to break off the connection
        temp = second.next
        second.next = None
        second = temp

        # recursively split our list until one node left
        first = self.sortList(first)
        second = self.sortList(second)

        return self.mergeList(first, second)

    # write a function to get the mid as we want to break apart the node
    def getMid(self, head):

        # 1 -> 2 -> 3 -> 4 -> 5
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow is the first half
        return slow

    # merge function
    def mergeList(self, first, second):

        # we can use a dummy node to have access to the head of merged list
        curr = dummy = ListNode()

        while first and second:

            if first.val < second.val:
                curr.next = first
                first = first.next
            else:
                curr.next = second
                second = second.next

            # move our pointer
            curr = curr.next

        curr.next = first or second

        return dummy.next
