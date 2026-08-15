# Remove Nth Node From End of List (Medium)
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Accepted 2026-08-15 — Python3, runtime 0 ms, memory 19.1 MB
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        we have a fast and a slow, we move the fast n times
        then begin to move the slow
        then set slow equal to the fast

        '''
        dummy=ListNode()
        tail=dummy
        dummy.next=head
        
        fast=head
        slow=dummy
        
        for i in range(n):
            fast=fast.next
        
        while fast:
            fast=fast.next
            slow=slow.next
           

        slow.next=slow.next.next

        return dummy.next
