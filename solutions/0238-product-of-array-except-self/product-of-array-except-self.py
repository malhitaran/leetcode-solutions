# Product of Array Except Self (Medium)
# https://leetcode.com/problems/product-of-array-except-self/
# Accepted 2026-07-30 — Python3, runtime 26 ms, memory 27.2 MB
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        #prefix
        prev=1
        pref=[]
        for num in nums:
            pref.append(prev)
            prev=prev*num

        print(pref)


        '''



        '''



        #suffix

        prev=1
        suf=[0]*len(nums)
        for i in range(len(nums)-1, -1, -1):
        
            suf[i]=prev
            prev=prev*nums[i]


        for i in range(len(nums)):
            suf[i]=suf[i]*pref[i]

        return suf
