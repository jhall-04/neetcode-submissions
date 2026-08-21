# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        f, l = head, head
        for i in range(n):
            l = l.next
        if not l:
            return head.next
        prev = None
        while l != None:
            prev = f
            f = f.next
            l = l.next
        prev.next = f.next
        return head

        