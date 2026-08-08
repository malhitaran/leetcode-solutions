# Decode String (Medium)
# https://leetcode.com/problems/decode-string/
# Accepted 2026-08-08 — Python3, runtime 0 ms, memory 19.5 MB
class Solution:
    def decodeString(self, s: str) -> str:
        
        '''
        3[a]2[bc]

        arr=[]
        stack=[]

        until theres a closing bracket

        '''
        res=[]
        stack=[]
        temp=[]

        for char in s:
            temp=[]
            if char!=']':
                stack.append(char)
            else:
                x=stack.pop()
                while stack and not x.isdigit():
                    if x!='[':
                        temp.append(x)
                    x=stack.pop()
                while stack and stack[-1].isdigit():
                    x= stack.pop()+x

                temp.reverse()
                for c in int(x)*temp:
                    stack.append(c)

            
                
            
            print(stack)
           
        return ''.join(stack)
