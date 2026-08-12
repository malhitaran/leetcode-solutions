# Daily Temperatures (Medium)
# https://leetcode.com/problems/daily-temperatures/
# Accepted 2026-08-12 — Python3, runtime 102 ms, memory 35.8 MB
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        '''
        HOW DO WE USE A STACK!!!

        stack.append every

        now while our num is greater than top stack
        r-l
        '''
        stack=[]
        res=[0]*len(temperatures)
        for i in range(len(temperatures)):

            
            while stack and temperatures[i]>stack[-1][0]:
                num, pos=stack.pop()
                res[pos]=(i-pos)
            
            stack.append((temperatures[i], i))
    
        return res
