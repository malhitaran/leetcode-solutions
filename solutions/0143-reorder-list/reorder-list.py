# Reorder List (Medium)
# https://leetcode.com/problems/reorder-list/
# Accepted 2026-06-28 — Python3, runtime 9 ms, memory 27.8 MB
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
        reverse the first list n
        then we move up by one for each list and modify it in turn and save the next node

        we only need half of each list

        Input: head = [1,2,3,4]

        1, 2
        4, 3

        1
        '''

        fast=head
        slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        second=slow.next
        slow.next=None

        prev=None
        curr=second
        count=0
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
            count+=1
        
        

        while prev:
            tmp1, tmp2=head.next, prev.next
            head.next=prev
            prev.next=tmp1
            head=tmp1
            prev=tmp2
        return head
