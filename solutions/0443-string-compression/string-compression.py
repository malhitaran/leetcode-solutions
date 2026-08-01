# String Compression (Medium)
# https://leetcode.com/problems/string-compression/
# Accepted 2026-08-01 — Python3, runtime 3 ms, memory 19.4 MB
class Solution:
    def compress(self, chars: List[str]) -> int:
        i=0
        count=0
        left=0
        while i<len(chars):
            current_char=chars[i]
            count=0

            while i < len(chars) and current_char==chars[i]:
                i+=1
                count+=1
            
            chars[left]=current_char
            left+=1
            if count>1:
                count=str(count)
                for x in range(len(count)):
                    chars[left]=count[x]
                    left+=1
        return left
