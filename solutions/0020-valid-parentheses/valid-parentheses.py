# Valid Parentheses (Easy)
# https://leetcode.com/problems/valid-parentheses/
# Accepted 2026-08-01 — Python3, runtime 0 ms, memory 19.3 MB
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

            if char=="(" or char=="{" or char=="[":
                stack.append(char)
            else:
                if stack:
                    x=stack.pop()
                else:
                    return False
                if pairOfBrackets[char]!=x:
                    return False

        if stack:
            return False
        else: return True
