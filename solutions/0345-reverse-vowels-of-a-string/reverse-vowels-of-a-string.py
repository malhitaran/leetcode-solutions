# Reverse Vowels of a String (Easy)
# https://leetcode.com/problems/reverse-vowels-of-a-string/
# Accepted 2026-05-16 — Python3, runtime 23 ms, memory 20.6 MB
class Solution:
    def reverseVowels(self, s: str) -> str:


        '''
        "IceCreAm"


        '''
        s=list(s)
        front=0
        back=len(s)-1

        vowels=["A","E","I","O","U","a","e","i","o","u",]
        while front<back:

            if s[front] in vowels and s[back] in vowels:
                temp=s[front]
                s[front]=s[back]
                s[back]=temp
                front+=1
                back-=1

            if s[front] not in vowels:
                front+=1
            
            if s[back] not in vowels:
                back-=1

        return ''.join(s)
