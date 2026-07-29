# Greatest Common Divisor of Strings (Easy)
# https://leetcode.com/problems/greatest-common-divisor-of-strings/
# Accepted 2026-07-29 — Python3, runtime 1 ms, memory 19.5 MB
import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if str1+str2!=str2+str1:
            return ""

        a=len(str1)
        b=len(str2)

        ourLen=gcd(a,b)
       

        return str1[:ourLen]
