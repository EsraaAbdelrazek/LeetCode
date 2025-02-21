from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)  # Create a dummy node to handle edge cases
        dummy.next = head
        prev, curr = dummy, head

        while curr:
            if curr.val == val:
                prev.next = curr.next  # Remove the node by skipping it
            else:
                prev = curr  # Move previous pointer only if no deletion
            curr = curr.next  # Move current pointer

        return dummy.next  # Return new head
