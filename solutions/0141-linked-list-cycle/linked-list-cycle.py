# Linked List Cycle (Easy)
# https://leetcode.com/problems/linked-list-cycle/
# Accepted 2026-06-28 — Python3, runtime 51 ms, memory 22.4 MB
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow=head
        fast=head

        while fast and fast.next:

            slow=slow.next
            fast=fast.next.next

            if slow==fast:
                return True

        return False
