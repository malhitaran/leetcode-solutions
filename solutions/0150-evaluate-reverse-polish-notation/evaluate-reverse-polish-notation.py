# Evaluate Reverse Polish Notation (Medium)
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Accepted 2026-08-12 — Python3, runtime 3 ms, memory 20.7 MB
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        my general idea

        we push until a operator
        when there is a operator we pop 2 elements off
        we do the calculation
        push back on
        continue

        '''
        
        stack=[]

        for token in tokens:
            if token.lstrip('-').isdigit():
                stack.append(int(token))
            else:
                x=stack.pop()
                y=stack.pop()
                if token=="/":
                    stack.append(int(y/x))
                if token=="*":
                    stack.append(int(floor(y*x)))
                if token=="-":
                    stack.append(int(floor(y-x)))
                if token=="+":
                    stack.append(int(floor(y+x)))
                   

        return stack[0]
