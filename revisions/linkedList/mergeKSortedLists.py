# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # merge sort
        # take pairs of list and just merge

        # edge cases are if we have empty or null lists
        if not lists or len(lists) == 0:
            return None

        # keep merging in pairs while lists > 1

        while len(lists) > 1:

            mergedList = []

            for i in range(0, len(lists), 2):

                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None

                # merge
                mergedList.append(self.mergeLists(l1, l2))

            lists = mergedList

        return lists[0]

    def mergeLists(self, l1, l2):

        curr = dummy = ListNode()

        while l1 and l2:

            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            curr = curr.next

        curr.next = l1 or l2

        return dummy.next
