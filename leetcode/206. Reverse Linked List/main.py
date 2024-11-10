# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        forward_list = []

        while head:
            forward_list.append(head.val)
            head = head.next
        
        results_linked_list = ListNode(None)
        tail = results_linked_list
        for i in reversed(forward_list):
            tail.next = ListNode(i)
            tail = tail.next
        
        return results_linked_list.next
