# Evaluate Reverse Polish Notation (Medium)
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Accepted 2026-06-17 — Python3, runtime 4 ms, memory 20.8 MB
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        '''
        ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

        we have the list of numbers
        we push them one by one onto the stack, each elemtns get put on once and popped once

        '''
        if len(tokens)==1:
            return int(tokens[0])
        
        stack=[]
        for operand in tokens:

            if operand=="+":
                y=stack.pop()
                x=stack.pop()
                stack.append(int(x)+int(y))
                
            elif operand=="-":
                y=stack.pop()
                x=stack.pop()
                stack.append(int(x)-int(y))
            elif operand=="*":
                y=stack.pop()
                x=stack.pop()
                stack.append(int(x)*int(y))
            elif operand=="/":
                y=stack.pop()
                x=stack.pop()
                z=float(int(x)/int(y))
                if z<0:
                    z=int(ceil(z))
                else:
                    z=int(floor(z))
                stack.append(z)
                print(stack)
            else:
                stack.append(operand)

        return stack[0]

'''

-132
6
10
'''
