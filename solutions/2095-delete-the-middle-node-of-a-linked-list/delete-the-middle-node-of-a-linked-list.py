# Delete the Middle Node of a Linked List (Medium)
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
# Accepted 2026-08-10 — Python3, runtime 67 ms, memory 63 MB
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy=ListNode()
        dummy.next=head
        count=0
        
        fast,slow=head,head
        prev=head


        while fast and fast.next:
            prev=slow
            slow=slow.next

            fast=fast.next.next


        if prev and prev.next:
            prev.next=prev.next.next
        else:
            return dummy.next.next

        return head
