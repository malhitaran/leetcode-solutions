# Greatest Common Divisor of Strings (Easy)
# https://leetcode.com/problems/greatest-common-divisor-of-strings/
# Accepted 2025-09-09 — Python3, runtime 0 ms, memory 17.8 MB
from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        gcd_len = gcd(len(str1), len(str2))
        return str1[:gcd_len]
