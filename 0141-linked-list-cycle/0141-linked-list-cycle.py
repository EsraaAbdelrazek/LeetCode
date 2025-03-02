# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = ListNode () 
        node.next = head 
        slow = fast = node 

        while fast and fast.next : 
            fast = fast.next.next 
            slow = slow.next 

            if fast is slow : 
                return True 
        return False 


        