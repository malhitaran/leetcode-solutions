# Car Fleet (Medium)
# https://leetcode.com/problems/car-fleet/
# Accepted 2026-08-13 — Python3, runtime 227 ms, memory 46.1 MB
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        stack=[]
        comb=[]
        for x in range(len(speed)):
            comb.append((position[x],speed[x]))
        comb.sort()
        for i in range(len(position)):
            pos,sp=comb[i][0],comb[i][1]
            it=(target-pos)/sp
            while stack and sp<stack[-1][1] and it>=stack[-1][2]:
                stack.pop()
            stack.append((pos,sp,it))
        return len(stack)
