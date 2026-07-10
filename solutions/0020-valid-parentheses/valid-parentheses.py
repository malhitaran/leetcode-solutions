# Valid Parentheses (Easy)
# https://leetcode.com/problems/valid-parentheses/
# Accepted 2026-07-10 — Python3, runtime 0 ms, memory 19.4 MB
class Solution:
    def isValid(self, s: str) -> bool:
        

        '''


        '''

        pairOfBrackets={

            ')':'(',
            '}':'{',
            ']':'['

        }


        stack=[]


        for char in s:

            if char in pairOfBrackets:
                if stack:
                    x=stack.pop()
                elif not stack:
                    return False
                if x!= pairOfBrackets[char]:
                    return False

            else:
                stack.append(char)

        if stack: 
            return False
        else:
            return True
