# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        t, h = head, head.next
        while h and h.next:
            t = t.next
            h = h.next.next

        second = t.next
        prev = t.next = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        second = prev
        cur = head
        while second:
            temp1, temp2 = cur.next, second.next
            cur.next = second
            second.next = temp1
            cur = temp1
            second = temp2
        





            
        