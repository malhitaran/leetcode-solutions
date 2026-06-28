# Add Two Numbers (Medium)
# https://leetcode.com/problems/add-two-numbers/
# Accepted 2026-06-28 — Python3, runtime 4 ms, memory 19.2 MB
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        '''
        we go n times

        we add the values, if its less than 10 perfect we store it as a new node with that value

        if its greater than 10 we carry 

        [9,9,9,9,9,9,9], 
        [9,9,9,9]
        8, 9, 9 9, 0, 0, 0, 1
        we need to do it from the bigger list
        '''
        dummy=ListNode()
        curr=dummy
        carry=0
        while l1 or l2 or carry:
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0

            currSum=v1+v2+carry
            carry=currSum //10
            value=currSum%10
            curr.next=ListNode(value)

            curr=curr.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None

        return dummy.next
