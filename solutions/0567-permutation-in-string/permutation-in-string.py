# Permutation in String (Medium)
# https://leetcode.com/problems/permutation-in-string/
# Accepted 2026-08-15 — Python3, runtime 15 ms, memory 19.4 MB
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        '''
        so we will keep a counter
        reduce when we see
        if we dont see just skip

        '''
        s1c,s2c,matches, l=[0]*26,[0]*26, 0,0
        if len(s1)>len(s2):
            return False
        for i in range(len(s1)):
            s1c[ord(s1[i])-ord('a')]+=1
            s2c[ord(s2[i])-ord('a')]+=1
        for i in range(26):
            matches+=1 if s1c[i]==s2c[i] else 0
        for r in range(len(s1), len(s2)):
            if matches==26:
                return True
            index=ord(s2[r])-ord('a')
            s2c[index]+=1
            if s2c[index]==s1c[index]:
                matches+=1
            elif s1c[index]+1==s2c[index]:
                matches-=1
        
            index=ord(s2[l])-ord('a')
            s2c[index]-=1
            if s2c[index]==s1c[index]:
                matches+=1
            elif s1c[index]-1==s2c[index]:
                matches-=1
            l+=1
        
        return matches==26
