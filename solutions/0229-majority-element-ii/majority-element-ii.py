# Majority Element II (Medium)
# https://leetcode.com/problems/majority-element-ii/
# Accepted 2026-08-05 — Python3, runtime 19 ms, memory 22.6 MB

from collections import Counter

'''

nums =
[3,2,,2,3, 6,5]

okay so the idea is that there can only ever be 2 elements that are the max

if you think about it carefully.

so what we can do is store a 2 elemetn hashmap. this hashmap can never get bigger than 2. when it does that means we subtract 1 from each count, this will get rid of the least frequent. you have to remember mathematically there can only be 2 maximum that meets the greater than n

i think the part that caught me our was checking in the final part

also we need a more systematic approach



then we go through the elements 1 by 1 and we count 

'''


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        numCount=defaultdict(int)
        res=[]
        for num in nums:

            numCount[num]+=1

            if len(numCount)<=2:
                continue

            tempDict = defaultdict(int)
            for n, count in numCount.items():
                if count>1:
                    tempDict[n]=count-1
                
            numCount=tempDict
        
        for val in numCount.keys():
            if nums.count(val) > len(nums)//3:
                res.append(val)
        
        return res
