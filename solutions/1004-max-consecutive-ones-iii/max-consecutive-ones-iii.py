# Max Consecutive Ones III (Medium)
# https://leetcode.com/problems/max-consecutive-ones-iii/
# Accepted 2026-08-06 — Python3, runtime 159 ms, memory 22.4 MB
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        '''
        [1,1,1,0,0,0,1,1,1,1,0]
        
        l r 


        while k<0:
            l+=1
            if l is 0 then cnt+=1

        '''

        l,cnt,res=0,0,0
        
        for r in range(len(nums)):

            if nums[r] == 1:
                cnt+=1
            else:
                k-=1
                cnt+=1
                while k<0:
                    print('yes')
                    print(nums[l])
                    if nums[l]==0:
                        
                        k+=1
                    cnt-=1
                    l+=1
                
            
            res=max(res, cnt)

        return res
