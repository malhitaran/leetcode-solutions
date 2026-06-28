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

            dummy=ListNode()
            dummy.next=head

            fast=dummy
            slow=dummy

            for _ in range(n+1):
                fast=fast.next

            while fast:
                slow=slow.next
                fast=fast.next

            slow.next=slow.next.next

            return dummy.next
