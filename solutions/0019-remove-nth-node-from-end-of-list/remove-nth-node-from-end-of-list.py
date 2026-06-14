# Remove Nth Node From End of List (Medium)
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Accepted 2026-06-14 — Python3, runtime 2 ms, memory 19.3 MB
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
            
            curr = head
            prev=curr
            counter=0

            while curr:
                counter += 1
                curr=curr.next
                
            
            diff=counter-n
            
            curr = head 
            for i in range(diff-1):
                curr = curr.next
            
            print(curr, counter)

            if diff == 0:
                return head.next
            nxt = curr.next.next
            curr.next = nxt

            return head




            '''
            while i!=diff:
                prevP=currP
                currP=currP.next
                i+=1
                
            prevP.next=currP.next

            return head
            '''
