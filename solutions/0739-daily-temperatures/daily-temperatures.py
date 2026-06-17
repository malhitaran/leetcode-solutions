# Daily Temperatures (Medium)
# https://leetcode.com/problems/daily-temperatures/
# Accepted 2026-06-17 — Python3, runtime 93 ms, memory 35.3 MB
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        optimised n squared solution by just skipping over steps

        '''
        answers=[0]*len(temperatures)
        stack=[]
        for i, temp in enumerate(temperatures):
            while stack and temp>stack[-1][1]:
                ansI, ansTemp=stack.pop()
                answers[ansI]=i-ansI
            stack.append((i,temp))
                
        return answers
