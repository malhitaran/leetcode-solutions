# Asteroid Collision (Medium)
# https://leetcode.com/problems/asteroid-collision/
# Accepted 2026-08-08 — Python3, runtime 3 ms, memory 20.4 MB
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        '''
        we know it collecides only in one condition when there was a right before the new left
        '''

        stack=[]

        for num in asteroids:
            
            if num>=0:
                stack.append(num)
                continue
            else:
                while stack and stack[-1]>0 and -num>stack[-1]:
                    stack.pop()
                if stack and stack[-1]>0 and -num==stack[-1]:
                    stack.pop()
                    continue
                if (stack and stack[-1]<0) or not stack:
                    stack.append(num)

        return stack
