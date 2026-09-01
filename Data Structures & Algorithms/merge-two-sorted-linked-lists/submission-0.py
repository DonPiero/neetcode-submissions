# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        l, r = list1, list2

        if not list1:
            return list2
        elif not list2:
            return list1 

        if l.val < r.val:
            head = l
            l = l.next
        else:
            head = r
            r = r.next        

        curr = head

        while l and r:
            if l.val < r.val:
                curr.next = l
                curr = l
                l = l.next
            else:
                curr.next = r
                curr = r
                r = r.next

        while l: 
            curr.next = l
            curr = l
            l = l.next

        while r: 
            curr.next = r
            curr = r
            r = r.next
        
        return head