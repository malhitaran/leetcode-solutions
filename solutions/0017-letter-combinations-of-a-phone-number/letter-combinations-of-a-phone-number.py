# Letter Combinations of a Phone Number (Medium)
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Accepted 2026-07-05 — Python3, runtime 0 ms, memory 19.1 MB
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        numToLetter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
            
        res=[""]
        def recurs(digit):
            nonlocal res
            temp=[]
            for letter in numToLetter[digit]:
                for word in res:
                    temp.append(word+letter)

            res=temp

        
        for digit in digits:
            recurs(digit)

        return res
