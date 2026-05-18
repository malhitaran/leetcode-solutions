# Container With Most Water (Medium)
# https://leetcode.com/problems/container-with-most-water/
# Accepted 2026-05-18 — Python3, runtime 67 ms, memory 29.7 MB
class Solution:
    def maxArea(self, height: List[int]) -> int:
        

        '''
        [1,8,6,2,5,4,8,3,7]


        width =  current indexs minus eachother
        '''

        first=0
        back=len(height)-1
        currBest=0

        while first<back:
            width=back-first
            length=min(height[first], height[back])
            currBest=max(currBest, width*length)
            

            if height[first]>height[back]:
                back-=1
            else:
                first+=1
        return currBest
