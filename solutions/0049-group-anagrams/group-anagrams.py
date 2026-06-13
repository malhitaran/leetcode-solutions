# Group Anagrams (Medium)
# https://leetcode.com/problems/group-anagrams/
# Accepted 2026-06-13 — Python3, runtime 19 ms, memory 24.1 MB

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        '''
        "nat","tan"

        we create a frequency dict
        where the keys are the frequency
        thne we put the strs as the values
        '''
        count= [0]* 26
        ourDict=dict()
        for i in range(len(strs)):
            count= [0]* 26
            for j in range(len(strs[i])):
                x=ord(strs[i][j])-ord('a')
                count[x]+=1
            count=tuple(count)
            if count in ourDict:
                ourDict[count].append(strs[i])
            else:ourDict[count]=[strs[i]]

        return list(ourDict.values())
