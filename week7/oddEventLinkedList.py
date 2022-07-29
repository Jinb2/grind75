class Solution:
    def oddEvenList(self, head):

        # separate odd and even linked list
        dummy1 = even = ListNode(0)
        dummy2 = odd = ListNode(0)

        while head:

            even.next = head.next

            odd.next = head

            even = even.next
            odd = odd.next

            head = head.next.next if even else None

        odd.next = dummy1.next  # pointing to even

        return dummy2.next

        """
        create even and odd dummy nodes
        curr ptr to move along the main linked list
        
        iterate through our linked list and while its not null

        if even connect to even list
        if odd connect to odd list 
        move respective pointers

        finally connect the two
        """
