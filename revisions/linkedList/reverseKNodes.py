# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # create a dummy node
        dummy = ListNode(0, head)

        # initially groupPrev is gonna be dummy
        groupPrev = dummy

        # we can just do while true
        while True:

            kth = self.getKth(groupPrev, k)
            # when kth doesnt exist
            if not kth:
                break

            # lets store the connection to the next node
            groupNext = kth.next

            # start reversing the list
            prev, curr = groupNext, groupPrev.next

            while curr != groupNext:
                # store connection to the next node
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp

        return dummy.next

    def getKth(self, node, k):

        curr = node

        while curr and k > 0:
            k -= 1
            curr = curr.next

        return curr
