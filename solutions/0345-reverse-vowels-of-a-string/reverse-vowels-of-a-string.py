# Reverse Vowels of a String (Easy)
# https://leetcode.com/problems/reverse-vowels-of-a-string/
# Accepted 2026-04-26 — Python3, runtime 28 ms, memory 20.7 MB
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        s=list(s)
        fp=0
        bp=len(s)-1


        '''
            Input
            s =
            "IceCreAm"
            Output
            "IcACreem"
            Expected
            "AceCreIm"
        '''
        while fp<bp:
            if s[fp] in vowels and s[bp] in vowels:
                #swap
                temp=s[fp]
                s[fp]=s[bp]
                s[bp]=temp
                fp+=1
                bp-=1
            elif s[fp] not in vowels:
                fp+=1
            elif s[bp] not in vowels:
                bp-=1

        return ''.join(s)
