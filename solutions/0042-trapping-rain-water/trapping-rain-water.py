# Trapping Rain Water (Hard)
# https://leetcode.com/problems/trapping-rain-water/
# Accepted 2026-06-18 — Python3, runtime 8 ms, memory 21.4 MB
class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        whilst its less we append

        if its greater we stop 
    

        '''

        stack=[]
        output=0
        for i in range(len(height)):
            while stack and height[i]>height[stack[-1]]:
                bottom=stack.pop()
                if not stack:
                    break
                left=stack[-1]
                width=i-left-1
                bounded=min(height[i], height[left]) - height[bottom]
                output+= width*bounded
            stack.append(i)
        return output
