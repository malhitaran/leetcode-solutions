# Baseball Game (Easy)
# https://leetcode.com/problems/baseball-game/
# Accepted 2026-08-24 — Python3, runtime 60 ms, memory 19.7 MB
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        

        stack=[]

        for ch in operations:
           
            print(stack)
            if ch.lstrip('-').isdigit():
                stack.append(int(ch))
            if ch=="+":
                stack.append(stack[-1]+stack[-2])
            if ch=="D":
                stack.append(stack[-1]*2)
            if ch=="C":
                stack.pop()
        print(stack)
        return sum(stack) if stack else 0
