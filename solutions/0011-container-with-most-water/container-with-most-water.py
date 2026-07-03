# Container With Most Water (Medium)
# https://leetcode.com/problems/container-with-most-water/
# Accepted 2026-07-03 — Python3, runtime 57 ms, memory 29.5 MB
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left,right = 0,len(height)-1
        best=0
        

        while left<right:
            width=right-left
            ourHeight=min(height[left], height[right])
            best=max(best, width*ourHeight)

            if height[left]>height[right]:
                right-=1
            else:
                left+=1

        return best
