# Delete the Middle Node of a Linked List (Medium)
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
# Accepted 2026-03-10 — Python3, runtime 119 ms, memory 62.3 MB
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        count = 0

        while curr:
            count += 1
            curr = curr.next

        # special case: only one node
        if count == 1:
            return None

        prev = None
        curr = head

        for i in range(count // 2):
            prev = curr
            curr = curr.next

        prev.next = curr.next

        return head
