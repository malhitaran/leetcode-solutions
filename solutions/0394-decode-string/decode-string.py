# Decode String (Medium)
# https://leetcode.com/problems/decode-string/
# Accepted 2026-03-09 — Python3, runtime 1 ms, memory 19.3 MB
class Solution:
    def decodeString(self, s: str) -> str:


        '''

        we will put until a close bracket, then pop until a open bracket

        
        '''
        stack=[]
        for char in s:
            tempS=""
            mul=""
            if char!="]":
                stack.append(char)
            else: 
                while stack[-1]!="[":
                    tempS+=stack.pop()
                tempS=tempS[::-1]
                stack.pop()
                while stack and stack[-1].isdigit():
                    mul+=stack.pop()
                mul=int(mul[::-1])
                stack.extend(mul*tempS)
                

                    
        

        return ''.join(stack)
