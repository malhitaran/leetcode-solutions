# Maximum Twin Sum of a Linked List (Medium)
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
# Accepted 2026-03-11 — Python3, runtime 62 ms, memory 50.7 MB
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        # Step 1: find middle
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: reverse second half
        prev = None
        curr = slow
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # Step 3: compute twin sums
        max_sum = 0
        first = head
        second = prev
        
        while second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next
        
        return max_sum
