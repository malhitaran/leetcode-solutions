# Add Two Numbers (Medium)
# https://leetcode.com/problems/add-two-numbers/
# Accepted 2026-06-28 — Python3, runtime 3 ms, memory 19.3 MB
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        '''
        we go n times

        we add the values, if its less than 10 perfect we store it as a new node with that value

        if its greater than 10 we carry 

        [9,9,9,9,9,9,9], 
        [9,9,9,9]
        8, 9, 9 9, 0, 0, 0, 1
        we need to do it from the bigger list
        '''

        #find bigger list

        curr1=l1
        count1=0
    
        while curr1:
            curr1=curr1.next
            count1+=1

        curr2=l2
        count2=0
        mark1=False
    
        while curr2:
            curr2=curr2.next
            count2+=1
        
        if count1>=count2:
            curr=l1
            other=l2
            mark1=True
        else:
            curr=l2
            other=l1

        carry=0
        prev=None
        while curr:
            if other!=None:

                ourSum=curr.val+other.val+carry
                other = other.next
            else:
                ourSum=curr.val+carry

            if ourSum>=10:
                #carry the first digit
                curr.val=int(str(ourSum)[1])
                carry=int(str(ourSum)[0])
                
            else:
                curr.val=ourSum
                carry=0
            prev=curr
            curr=curr.next
            
        if carry>0:
            prev.next=ListNode(val=carry, next=None)
        return l1 if mark1 else l2

        '''
        curr=head

        while curr:

        '''
