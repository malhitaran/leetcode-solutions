# Two Sum II - Input Array Is Sorted (Medium)
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Accepted 2026-08-13 — Python3, runtime 5 ms, memory 20.5 MB
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        '''
        constant extra space is tricky

        i identified it was two pointers if were using no extra space

        main idea we have a target

        if our sum is less than then we decrement 
        vice versa

        '''

        l,r=0,len(numbers)-1

        while l<r:
            
            ourS=numbers[l]+numbers[r]
            if ourS==target:
                return [l+1, r+1]
            elif ourS<target:
                l+=1
            else:
                r-=1
