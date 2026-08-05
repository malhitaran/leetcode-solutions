# Majority Element II (Medium)
# https://leetcode.com/problems/majority-element-ii/
# Accepted 2026-08-05 — Python3, runtime 10 ms, memory 23.5 MB

from collections import Counter

'''
5 1 2 3 4 

'''
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        numFreq=Counter(nums)
        res=[]
        aThird=float(len(nums)/3)

        print(aThird)
        
        for num, freq in numFreq.items():
            if float(freq)>aThird:
                res.append(num)
        
        return res
