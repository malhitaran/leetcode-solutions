# Removing Stars From a String (Medium)
# https://leetcode.com/problems/removing-stars-from-a-string/
# Accepted 2026-03-08 — Python3, runtime 83 ms, memory 20.6 MB
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char == '*':
                stack.pop()  # remove previous char
            else:
                stack.append(char)
        return ''.join(stack)
