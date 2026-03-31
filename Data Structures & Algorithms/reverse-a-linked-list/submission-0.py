# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = None
        cur, n = head, head
        while cur != None:
            n = cur.next
            cur.next = p
            p = cur
            cur = n
        return p