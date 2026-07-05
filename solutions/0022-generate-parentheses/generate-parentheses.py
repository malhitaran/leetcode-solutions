# Generate Parentheses (Medium)
# https://leetcode.com/problems/generate-parentheses/
# Accepted 2026-07-05 — Python3, runtime 0 ms, memory 19.4 MB
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:


        '''


        '''


        res=[]


        opening=0
        closing=0


        def backtrack(open,close, curStr):

            if open==n and close==n:
                res.append(curStr)
                return

            if open<n:
                backtrack(open+1, close, curStr+"(")
            if close<open:
                backtrack(open, close+1, curStr+")")
            

        backtrack(0,0,"")
        return res
