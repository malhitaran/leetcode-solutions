# Valid Parentheses (Easy)
# https://leetcode.com/problems/valid-parentheses/
# Accepted 2026-06-15 — Python3, runtime 0 ms, memory 19.3 MB
class Solution:
    def isValid(self, s: str) -> bool:
        
        '''
        we can use a dictionary for the corresponding value e.g. key { value }
        we pop on teh stack whilst its ([{

        if we encoutner a })] then we pop and see if it matches

        if not fail
        else true

        '''
        stack=[]
        ourDict = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in s:
            if char=="[" or char=="{" or char=="(":
                stack.append(char)
            elif (char=="]" or char=="}" or char==")" ) and stack:
                if ourDict[char]!=stack.pop():
                    return False
            else:
                return False
                
        if stack:
            return False
        return True
