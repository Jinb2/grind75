class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # to reverse a linked list
        # we need some sort of way to have access to the previous node
        # so we can use a prev and curr pointer to access two nodes we want to reverse
        # this will take O(n)
        # there are things we have to consider which is when do we stop and are there any edge cases
        # edge case is going to be if we are given a null node and in that case we can just return the head
        # we know when  to stop when the pointer is Null

        # edge case
        if not head:
            return head

        prev, curr = None, head

        while curr:
            # we want to store a pointer to next node as a way to traverse to it
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
