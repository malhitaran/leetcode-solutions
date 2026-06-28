# Linked List Cycle (Easy)
# https://leetcode.com/problems/linked-list-cycle/
# Accepted 2026-06-28 — Python3, runtime 65 ms, memory 22.8 MB
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        ourS=set()
        curr=head

        while curr:
            if curr in ourS:
                return True
            else:
                ourS.add(curr)

            curr=curr.next

        return False
