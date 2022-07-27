class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        slow, fast = head, head

        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        # reverse starting from slow
        prev = None

        while slow:

            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        start = head

        while prev:

            if prev.val != start.val:
                return False

            start = start.next
            prev = prev.next

        return True
