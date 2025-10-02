# Reverse Vowels of a String (Easy)
# https://leetcode.com/problems/reverse-vowels-of-a-string/
# Accepted 2025-10-02 — Python3, runtime 24 ms, memory 18.8 MB
class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        newWord=[]
        length=len(s)
        listOfVowels=[char for char in s if char in vowels]
        
        for char in s:
            if char in vowels:
                newWord.append(listOfVowels.pop())
            else:
                newWord.append(char)

        return ''.join(newWord)
