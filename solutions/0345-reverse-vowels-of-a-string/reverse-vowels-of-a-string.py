# Reverse Vowels of a String (Easy)
# https://leetcode.com/problems/reverse-vowels-of-a-string/
# Accepted 2026-07-29 — Python3, runtime 11 ms, memory 21.3 MB
class Solution:
    def reverseVowels(self, s: str) -> str:

            '''

            two pointer solution

            '''

            vowels={'A', 'a', 'E', 'e','I', 'i','O', 'o','U', 'u'}

            end=len(s)-1
            start=0

            s=list(s)
            print(s)
            
            while start<end:

                if s[start] in vowels and s[end] in vowels:
                    temp=s[start]
                    
                    s[start]=s[end]
                    s[end]=temp
                    start+=1
                    end-=1
                if s[start] not in vowels:
                    start+=1
                if s[end] not in vowels:
                    end-=1
           
            return ''.join(s)
