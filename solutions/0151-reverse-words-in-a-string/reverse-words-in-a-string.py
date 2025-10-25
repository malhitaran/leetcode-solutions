# Reverse Words in a String (Medium)
# https://leetcode.com/problems/reverse-words-in-a-string/
# Accepted 2025-10-25 — Python3, runtime 0 ms, memory 17.9 MB
class Solution:
    def reverseWords(self, s: str) -> str:
        newString=""
        words=s.split()
        print(words)
        n=len(words)-1
       
        while n>=0:
            if n==0:
                newString+=words[n]
            else:
                newString+=words[n]+" "
            n-=1
        return newString
