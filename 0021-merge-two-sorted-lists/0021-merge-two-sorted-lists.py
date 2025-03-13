class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to act as the starting point of the merged list
        dummy = ListNode(-1)
        current = dummy

        # Traverse both lists and merge them in sorted order
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # If there are remaining nodes in list1 or list2, append them
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # Return the merged list starting from the next node of dummy
        return dummy.next