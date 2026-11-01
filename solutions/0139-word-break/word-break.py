# Word Break (Medium)
# https://leetcode.com/problems/word-break/
# Accepted 2026-11-01 — Python3, runtime 2 ms, memory 19.3 MB
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:

        '''

        is there a path using this word that would lead to true? 

        what does the recursion look like??
        

        so we want to see if using this in addition leads to true

        so the map should contain combinatioins of words and there realm of outcomes

        we should start from the bottom like leet then we know code is false and leet is false

        store already solved problems and say there outcome 


        '''
        
        dp=[False]*(len(s)+1)
        dp[len(s)]=True

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if i+len(w)<=len(s) and s[i: i+ len(w)]== w:
                    dp[i]=dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]
