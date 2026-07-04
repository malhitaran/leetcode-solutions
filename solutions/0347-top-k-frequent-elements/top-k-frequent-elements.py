# Top K Frequent Elements (Medium)
# https://leetcode.com/problems/top-k-frequent-elements/
# Accepted 2026-07-04 — Python3, runtime 10 ms, memory 24.7 MB
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        
        '''

        bucket sort

        freq where its a list of a list


        [[]] and each index represents the count

        and at each index we have a list of numbers

        and then we go backwards

        '''


        valueFrequency=Counter(nums)

        frequency=[[] for i in range(len(nums)+1)]
        
        res=[]
        
        for num, count in valueFrequency.items():

            frequency[count].append(num)

       
        for i in range(len(nums), 0, -1):
           
            for num in frequency[i]:

                res.append(num)
                if len(res)==k:
                    return res
