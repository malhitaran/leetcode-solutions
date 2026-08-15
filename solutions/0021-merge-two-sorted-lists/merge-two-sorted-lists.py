# Merge Two Sorted Lists (Easy)
# https://leetcode.com/problems/merge-two-sorted-lists/
# Accepted 2026-08-15 — Python3, runtime 0 ms, memory 19.3 MB
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l3=ListNode(None)
        cur3=l3
        

        while l1 and l2:
            if l1.val<l2.val:
                cur3.next=l1
                l1=l1.next
            else:
                cur3.next=l2
                l2=l2.next
            cur3 = cur3.next
        cur3.next = l1 if l1 else l2

        return l3.next
