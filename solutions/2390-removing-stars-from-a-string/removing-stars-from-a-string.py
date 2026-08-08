# Removing Stars From a String (Medium)
# https://leetcode.com/problems/removing-stars-from-a-string/
# Accepted 2026-08-08 — Python3, runtime 85 ms, memory 20.4 MB
class Solution:
    def removeStars(self, s: str) -> str:


        stack=[]

        for char in s:

            if char !="*":
                stack.append(char)
            else:
                stack.pop()
        return ''.join(stack)
