# Asteroid Collision (Medium)
# https://leetcode.com/problems/asteroid-collision/
# Accepted 2026-03-08 — Python3, runtime 8 ms, memory 20.4 MB
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]

        for num in asteroids:
            if stack:
                if stack[-1]>=0 and num<0:
                    while stack and stack[-1] > 0 and num < 0 and abs(num) > stack[-1]:
                        stack.pop()
                    if stack and stack[-1]==abs(num):
                        stack.pop()
                    elif not stack or stack[-1] < 0:
                        stack.append(num)
                else:
                    stack.append(num)
            else:
                stack.append(num)


        return stack
