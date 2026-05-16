# Greatest Common Divisor of Strings (Easy)
# https://leetcode.com/problems/greatest-common-divisor-of-strings/
# Accepted 2026-05-16 — Python3, runtime 0 ms, memory 19.3 MB
import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        '''
        way 1
        brute force solution 

        '''

        shorter = str1 if len(str1)<len(str2) else str2

        for length in range(len(shorter), 0, -1):
            candidate=shorter[:length]

            if (len(str1) % len(candidate) ==0) and (len(str2) % len(candidate)==0):
                if (candidate * (len(str1) // length)==str1) and (candidate *(len(str2) // length)==str2):
                    return candidate

        return ""
