# Reverse Linked List (Easy)
# https://leetcode.com/problems/reverse-linked-list/
# Accepted 2026-03-10 — Python3, runtime 0 ms, memory 20.4 MB
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None

        stack = []
        curr = head

        # Push all nodes onto the stack
        while curr:
            stack.append(curr)
            curr = curr.next

        # Pop the new head
        new_head = stack.pop()
        curr = new_head

        # Rewire the rest
        while stack:
            curr.next = stack.pop()
            curr = curr.next

        # Terminate the list
        curr.next = None

        return new_head
