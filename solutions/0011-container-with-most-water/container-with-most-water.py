# Container With Most Water (Medium)
# https://leetcode.com/problems/container-with-most-water/
# Accepted 2026-06-20 — Python3, runtime 59 ms, memory 29.7 MB
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        start=0
        end=len(height)-1
        best=0
        while start<end:
            w = end-start
            h=min(height[end], height[start])
            best=max(best, w*h)
            if height[end]>height[start]:
                start+=1
            else:
                end-=1
        return best
