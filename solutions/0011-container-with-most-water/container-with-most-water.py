# Container With Most Water (Medium)
# https://leetcode.com/problems/container-with-most-water/
# Accepted 2026-06-11 — Python3, runtime 57 ms, memory 29.6 MB
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        '''


        [1,8,6,2,5,4,8,3,7]
        two pointers

        one at the front one at the back
        if 
        '''

        front=0
        back=len(height)-1
        best=0
        currBest=0
        while front<back:
            currBest=(back-front) * min(height[front],height[back])
            best=max(currBest,best)
            if height[front]>height[back]:
                back-=1
            else:
                front+=1

        return best
