# Majority Element (Easy)
# https://leetcode.com/problems/majority-element/
# Accepted 2026-09-05 — Python3, runtime 8 ms, memory 21 MB
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res,cnt=0,0
        for num in nums:
            if num==res:
                cnt+=1
            else:
                if cnt==0:
                    res=num
                    cnt=1
                else:
                    cnt-=1
        return res
