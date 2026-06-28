# Reverse Linked List (Easy)
# https://leetcode.com/problems/reverse-linked-list/
# Accepted 2026-06-28 — Python3, runtime 0 ms, memory 20.2 MB
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        '''
        [1,2,3,4,5]

        we go through one item at a time, save the next node, set it to the previous node
        '''

        prev=None
        curr=head
        while curr!=None:
       
            temp=curr.next
            
            curr.next=prev
            
            prev=curr
            
            curr=temp
           

        
        return prev
