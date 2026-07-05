# Letter Combinations of a Phone Number (Medium)
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Accepted 2026-07-05 — Python3, runtime 0 ms, memory 19.2 MB
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # Seed the lookup table (Typo on '7' is fixed, well done!)
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
            
        res = []
        
        # FIX 1: Definition must match intended use. (i progress, curStr built)
        def backtrack(i: int, current_string: str):
            # FIX: curStr definition managed locally (passed downwards)
            if len(current_string) == len(digits):
                res.append(current_string)
                return  # unused True removed

            # Loop over letters for current digit 'digits[i]'
            for letter in numToLetter[digits[i]]:
                # CALL now matches the logical flow in image_2.png
                # Progression 'i+1', String construction 'curStr+letter'
                backtrack(i+1, current_string + letter)

        # Initial call needs state: Start at index 0, with an empty string
        if digits:
            backtrack(0, "")  # FIX 2: Correct initial state (index 0)
        else:
            return []

        # FIX 3: Return the accumulated results!
        return res
