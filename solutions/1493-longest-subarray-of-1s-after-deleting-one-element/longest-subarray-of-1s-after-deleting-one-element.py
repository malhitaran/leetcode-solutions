# Longest Subarray of 1's After Deleting One Element (Medium)
# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
# Accepted 2026-08-06 — Python3, runtime 43 ms, memory 24.6 MB
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:


        '''

        [1,1,0,1]


        '''
        

        l, cnt, res=0,0,0
        k=1

        for r in range(len(nums)):

            if nums[r] ==1:
                cnt+=1
            else:
                k-=1
                while k<0:

                    if nums[l]==0:
                        k+=1
                    else:
                        cnt-=1
                    l+=1
            res=max(res, cnt)

        return res-1 if k==1 else res
