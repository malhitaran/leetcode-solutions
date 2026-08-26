# Majority Element (Easy)
# https://leetcode.com/problems/majority-element/
# Accepted 2026-08-26 — Python3, runtime 0 ms, memory 21.2 MB
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        '''
        bayes algo
        boyer moore***

        [2,2,1,1,1,2,2]
        '''
        curr=0
        count=0
        for num in nums:
            if num==curr:
                count+=1
            elif num!=curr and count!=0:
                count-=1
            else:
                curr=num
                res=1
        
        return curr
