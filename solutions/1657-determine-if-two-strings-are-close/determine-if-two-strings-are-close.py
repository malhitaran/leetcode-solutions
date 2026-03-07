# Determine if Two Strings Are Close (Medium)
# https://leetcode.com/problems/determine-if-two-strings-are-close/
# Accepted 2026-03-07 — Python3, runtime 189 ms, memory 20.5 MB
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        '''
        case 1:compare lengths of word 1 and word2 if there equal and the sets of both are equal(contain the same stuff and no difference) that means both sets have the same letters(by sets) and the same amount of words(by len)

        case 2:get the occurences if the occurence is the same and the set of words are the same then its fine


        aaabc   
        iiias
        aabbbbcc
        bca
        cccab set occur
        aaacb

        '''

        if len(word1)!=len(word2):
            return False

        dict1={}
        dict2={}
        
        for letter in word1:
            if letter not in dict1:
                dict1[letter]=1
            else:
                dict1[letter]+=1

        for letter in word2:
            if letter not in dict2:
                dict2[letter]=1
            else:
                dict2[letter]+=1
        
        

        if set(word1)==set(word2):
            if sorted(dict1.values()) == sorted(dict2.values()):
                return True
            else:
                return False
        else:
            return False
