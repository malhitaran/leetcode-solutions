# Container With Most Water (Medium)
# https://leetcode.com/problems/container-with-most-water/
# Accepted 2026-02-07 — Python3, runtime 63 ms, memory 29.7 MB
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        lhs=0
        rhs=len(height)-1
        max=0
        while lhs!=rhs:
            width=rhs-lhs
            hgt=min(height[lhs],height[rhs])
            val=width*hgt
            if val>max:
                max=val
            if height[lhs]>height[rhs]:
                rhs-=1
            elif height[rhs]>height[lhs]:
                lhs+=1
            elif height[rhs]==height[lhs]:
                lhs+=1
        return max
