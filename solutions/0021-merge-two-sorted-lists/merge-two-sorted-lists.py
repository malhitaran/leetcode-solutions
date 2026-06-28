# Merge Two Sorted Lists (Easy)
# https://leetcode.com/problems/merge-two-sorted-lists/
# Accepted 2026-06-28 — Python3, runtime 0 ms, memory 19.2 MB
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        '''
        list1 = [1,2,2], 
        list2 = [1,3,5,5,6]

        '''
        
        dummy=ListNode()
        pointer=dummy

        while l1 and l2:

            if l1.val<l2.val:
                pointer.next=l1
                l1=l1.next
            else:
                pointer.next=l2
                l2=l2.next
            
            pointer=pointer.next

        if l1:
            pointer.next=l1
        else:
            pointer.next=l2

        return dummy.next
