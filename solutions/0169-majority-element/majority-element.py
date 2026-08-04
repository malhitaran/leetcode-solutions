# Majority Element (Easy)
# https://leetcode.com/problems/majority-element/
# Accepted 2026-08-04 — Python3, runtime 3 ms, memory 21.1 MB
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        '''
        so the main idea of this was that because its a majority element basically we can do 0(1 complexity) for mem

        because of that idea only because we know one element will be the majority, which means over half are that number ONLY BECAUSE of that property, we know we can actually keep track of the most frequent element using o(1) memory complexity

        the idea works as follows
        we use a single count and the actually number represented
        say its 1,3,3,2,1,1. 

        res will start of at 1 
        count will be 1 because it occured 1 time.
        3 will decrement it to 0, 
        3 will become res and count will go to 1
        so on..
        until 1 is the stored best
        '''


        res, count=None, 0

        for num in nums:

            if count==0:
                res=num
            count+=(1 if num==res else -1)

        return res
