# House Robber (Medium)
# https://leetcode.com/problems/house-robber/
# Accepted 2026-11-01 — Python3, runtime 0 ms, memory 19.4 MB
class Solution:
    def rob(self, nums: list[int]) -> int:
        '''
        memoisation 

        so if we grab the next one will be at i+2

        say weve done a index before we dont want to recaluclate that index
        so how can we save time here

        0 -> 2

        '''
        seen={}
        def dfs(i):

            if i>=len(nums):
                return 0

            if i in seen:
                return seen[i]
                            
            seen[i]=max(nums[i]+ dfs(i+2), dfs(i+1))
            
            return seen[i]
        
        return dfs(0)
