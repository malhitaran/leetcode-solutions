# Reorder List (Medium)
# https://leetcode.com/problems/reorder-list/
# Accepted 2026-08-15 — Python3, runtime 3 ms, memory 27.7 MB
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        '''
        we can reverse the list and take the half integer division


        Input: head = [1,2,3,4]

                        4321

        12
        43


        [1,2,3,4,5]
        5 4 3 2 1

        123
        54

        '''
        
        slow,fast=head,head.next

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        #reverse now
        second=slow.next
        prev=slow.next=None
        while second:
            tmp=second.next
            second.next=prev
            prev=second
            second=tmp
        
        #merge
        second=prev
        first=head
        while second:
            tmp1, tmp2=first.next, second.next
            first.next=second
            second.next=tmp1
            first,second=tmp1, tmp2
        
        return head
