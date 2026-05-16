# Greatest Common Divisor of Strings (Easy)
# https://leetcode.com/problems/greatest-common-divisor-of-strings/
# Accepted 2026-05-16 — Python3, runtime 0 ms, memory 19.3 MB
import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        '''
        way 2
        optimal faang way 

        '''

        if str1+str2!=str2+str1:
            return ""

        length=gcd(len(str1), len(str2))

        
        return str1[:length]
