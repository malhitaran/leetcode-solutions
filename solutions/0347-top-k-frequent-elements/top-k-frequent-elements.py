# Top K Frequent Elements (Medium)
# https://leetcode.com/problems/top-k-frequent-elements/
# Accepted 2026-08-01 — Python3, runtime 11 ms, memory 24.8 MB
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        '''

        so we know we can create buckets 
        in these buckets we can store the numbers

        e.g. if we had 10 numbers we know a number cannot occur more than 10 times. 

        then we do a search backwards


        creating the bucket is easy

        '''
        res=[]
        numBucket=[[] for x in range(len(nums)+1)]
        freqNum=Counter(nums)

        for num, freq in freqNum.items():
            
            numBucket[freq].append(num)

        for ourBucket in reversed(numBucket):

            if k<=0:
                break
            else:
                for item in reversed(ourBucket):
                    res.append(item)
                    k-=1
                    if k<=0:
                        break
        return res
