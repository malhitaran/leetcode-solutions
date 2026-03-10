# Odd Even Linked List (Medium)
# https://leetcode.com/problems/odd-even-linked-list/
# Accepted 2026-03-10 — Python3, runtime 0 ms, memory 21.2 MB
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
       
        if not head or not head.next:
            return head  # 0 or 1 node, nothing to do

        odd = head              # first node is odd
        even = head.next        # second node is even
        even_head = even        # remember the start of even nodes

        while even and even.next:
            # connect odd nodes together
            odd.next = even.next
            odd = odd.next

            # connect even nodes together
            even.next = odd.next
            even = even.next

        # attach even list after odd list
        odd.next = even_head

        return head

        '''
                we do by two and set it the evens to equal eachother 
                then the last one points to the first odd
                now we do another pass setting the odds and last is null

                
                '''
