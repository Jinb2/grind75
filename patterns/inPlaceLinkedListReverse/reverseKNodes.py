class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)

        # node before this group we are reversing
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)

            if not kth:
                break

            groupNext = kth.next

            # groupPrev.next is the tail when reversed so it needs to point to groupnext.next
            prev, curr = kth.next, groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # we need to connect group prev to the kth
            # so store that before it is reconnected.
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp

        return dummy.next

    def getKth(self, curr, k):

        while curr and k > 0:
            curr = curr.next
            k -= 1

        return curr
