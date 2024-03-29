class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # get mid
        slow, fast = head, head.next

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        second = slow.next
        slow.next = None
        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge two halfs
        first, second = head, prev

        while second:

            temp1, temp2 = first.next, second.next

            first.next = second
            second.next = temp1
            first, second = temp1, temp2
