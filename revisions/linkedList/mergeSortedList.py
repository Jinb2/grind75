# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        # my goal is that i want to sort of compare the numbers between the sorted list
        # and depending on which is bigger connect it to a "dummy" list
        # how do i know which list i want to move forward? well the one that had the smaller values because
        # since it is sorted then all the elements after the larger element list will also be bigger than tthe current one
        # so here are my steps:
        # create a dummy list and pointer for it
        # we keep iterating until we finish one list
        # because once one list is done we can just append the remaining list to our dummy list
        # we always append the smaller value and it doesnt matter if the values are the same we can just append either one
        # finally since our dummy points to the head of the merged lsit we can jsut return dummy.next
        # edge case is if both lists are null then we can just return None

        # edge case
        if not list1 and not list2:
            return None

        # create our dummy node
        curr = dummy = ListNode()

        # as long as we have a list
        while list1 and list2:

            # compare values and move forward respective pointer
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:  # covers if they are equal
                curr.next = list2
                list2 = list2.next

            # we can move our curr ptr
            curr = curr.next

        # we might have remaining list since they might not be equal length
        # append the remaining
        curr.next = list1 or list2

        return dummy.next
