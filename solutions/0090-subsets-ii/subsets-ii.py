# Subsets II (Medium)
# https://leetcode.com/problems/subsets-ii/
# Accepted 2026-08-24 — Python3, runtime 0 ms, memory 19.4 MB
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        

        '''
        we can do a for loop with prev and move on 
        or we can do that while loop and move 

        ntil the index is not the same

        for loop is cleaner but harder to code
        while loop is more intuitive
        '''
        nums.sort()
        res=[]
        curr=[]
        def recurs(i,curr):

            if i>=len(nums):
                res.append(curr.copy())
                return

            curr.append(nums[i])
            recurs(i+1,curr)

            curr.pop()
            prev=nums[i]
            while i<len(nums) and nums[i]==prev:
                i+=1
            recurs(i,curr)

        recurs(0, [])
        return res
