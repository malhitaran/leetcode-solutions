# Asteroid Collision (Medium)
# https://leetcode.com/problems/asteroid-collision/
# Accepted 2026-08-08 — Python3, runtime 9 ms, memory 20.3 MB
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
                while stack and num<0 and stack[-1]>0 and abs(num)>abs(stack[-1]):
                    stack.pop()
                if stack and num<0 and stack[-1]>0 and abs(num)==abs(stack[-1]):
                    stack.pop()
                    continue
                if stack and num<0 and stack[-1]<0:
                    stack.append(num)
                if not stack:
                    stack.append(num)

        return stack
