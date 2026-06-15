# Longest Consecutive Sequence (Medium)
# https://leetcode.com/problems/longest-consecutive-sequence/
# Accepted 2026-06-15 — Python3, runtime 83 ms, memory 36.7 MB
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        '''
        use num-1 find that in the array

        so for every element see if 100-1 exists otherwise its not the start of the sequence

        we got o(1) if were looking for a value in the set



        we put everything into a set, for each elemetn we know if its a start becasue we can do nums-1 in set which is constant, then we look if 

        for each element we see if its the start of a sequence, if it is then we enter a for loop whilst the set is not empty then we remove from the setif its the start, look for a +1 and run a counter 

        '''
        ourSet=set(nums)
        best=0
        i=0

        while ourSet and i<len(nums):
            x=nums[i]
            count=1
            if x-1 not in ourSet:
                ourSet.discard(x)
                while x+1 in ourSet and ourSet:
                    count+=1
                    ourSet.remove(x+1)
                    x+=1
                if count>best:
                    best=count
            i+=1

        
        return best
