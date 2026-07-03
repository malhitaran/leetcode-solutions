# Valid Parentheses (Easy)
# https://leetcode.com/problems/valid-parentheses/
# Accepted 2026-07-03 — Python3, runtime 0 ms, memory 19.2 MB
class Solution:
    def isValid(self, s: str) -> bool:
        

        '''


        '''

        stack=[]

        bracketMapping={

            ')':'(',
            '}':'{',
            ']':'['
        }

        for bracket in s:

            if bracket=="(" or bracket=="{" or bracket=="[":
                stack.append(bracket)
            else:
                if stack:
                    lastBracket=stack.pop()
                else:
                    return False

                if bracketMapping[bracket]!=lastBracket:
                    return False

        if stack: 
            return False
        else:
            return True
