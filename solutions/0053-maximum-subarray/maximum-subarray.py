# Maximum Subarray (Medium)
# https://leetcode.com/problems/maximum-subarray/
# Accepted 2026-11-01 — Python3, runtime 57 ms, memory 31.1 MB
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        '''

        i think i got it, we expand whilst n is not bigger than our count

        if it is we shrink l until our curr is greater than n

        i think its stricktly greater than n, if it was equal we could have -2 and -2 that would make -4 

        if we think about it postives we would have 2 and 2 but then we would need to make it incude n 

        does adding n make it greater than the curr sum, so move l until n + curr sum is greater than curr sum

        now if n is negative -2 and curr sum was 02 we move l again because -4 is not greater than ,

        if that was postivie like 2 and 2, n + currsum is 4 so we dont move l foward anymore


        currSum=-2 

        5 4 -1 7 8

        cs=9
        cs 8
        15
        23

        cs=-1 

        '''

        if len(nums)==1:
            return nums[0]
        else:
            currSum=nums[0]
            l,res=0, currSum

        for r in range(1, len(nums)):
            while currSum + nums[r] < nums[r]:
                currSum-=nums[l]
                l+=1
            
            currSum+=nums[r]
            res=max(res, currSum)
            

        return res
