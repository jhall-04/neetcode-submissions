# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None
        if n == 1:
            return lists[0]
        if n == 2:
            return merge2(lists[0], lists[1])
        return merge2(self.mergeKLists(lists[:n//2]), self.mergeKLists(lists[n//2:]))

def merge2(list1, list2):
    res = cur = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next
    if list1:
        cur.next = list1
    else:
        cur.next = list2
    return res.next
