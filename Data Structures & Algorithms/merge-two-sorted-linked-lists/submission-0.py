# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Empty Check
        if not list1:
            return list2
        if not list2:
            return list1
        
        # Set head and iterator node
        head = None
        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        cur = head

        # Iterate through
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                cur = list1
                list1 = list1.next
            else:
                cur.next = list2
                cur = list2
                list2 = list2.next
        
        # Append end of other list
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        
        return head