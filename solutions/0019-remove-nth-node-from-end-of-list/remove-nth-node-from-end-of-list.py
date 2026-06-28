# Remove Nth Node From End of List (Medium)
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Accepted 2026-06-28 — Python3, runtime 0 ms, memory 19.3 MB
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

            curr=head
            count=0
            while curr:
                count+=1
                curr=curr.next
            print(count)
        
            dummy=ListNode()
            dummy.next=head
            curr=dummy
            
            if count-n==0:
                return head.next
            
            for i in range(count-n):
                curr=curr.next
            
            curr.next=curr.next.next
            return dummy.next
