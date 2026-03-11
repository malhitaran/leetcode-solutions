# Maximum Twin Sum of a Linked List (Medium)
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
# Accepted 2026-03-11 — Python3, runtime 69 ms, memory 63.2 MB
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        if not head:
            return head
    
        '''
        use stack
        push all elements to stack
        then compare top elemetn and current start element if its max
        '''
        curr = head
        stack = []

        while curr:
            stack.append(curr)
            curr = curr.next

        curr = head
        maxS = 0

        while stack:
            twin = stack.pop()
            maxS = max(maxS, curr.val + twin.val)
            curr = curr.next

        return maxS
