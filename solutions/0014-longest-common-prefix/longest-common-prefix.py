# Longest Common Prefix (Easy)
# https://leetcode.com/problems/longest-common-prefix/
# Accepted 2026-08-04 — Python3, runtime 0 ms, memory 19.2 MB
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        '''
w       we take the max one and thats our comparison
        then we go through each character
        if we ever hit 0 return

        otherwise we go through 

        actually much more efficient 

        we compare 0 in every o

        '''
        

        #get the min

        #nk

        smallest=float('infinity')

        for word in strs:
            smallest=min(smallest, len(word))


        for charNum in range(smallest):
            ourS=set()
            for word in strs:
                ourS.add(word[charNum])
            
            if len(ourS)>=2:
                
                return strs[0][:charNum]
        
        
        return strs[0][:smallest]
