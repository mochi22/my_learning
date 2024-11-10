# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel = ListNode()
        results = sentinel
        current = head
        remove_value = None

        while current:
            if remove_value == current.val:
                current = current.next
                continue
            if current.next and current.val == current.next.val:
                remove_value = current.val
                continue
            else:
                results.next = current
                results = results.next
                current = current.next
        results.next = None
        # print("@@@@\n", sentinel)
        return sentinel.next
