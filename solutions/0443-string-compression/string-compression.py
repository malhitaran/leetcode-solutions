# String Compression (Medium)
# https://leetcode.com/problems/string-compression/
# Accepted 2026-08-01 — Python3, runtime 0 ms, memory 19.3 MB
class Solution:
    def compress(self, chars: List[str]) -> int:

        left=0
        prev=''
        count=0
        
        for i,char in enumerate(chars):

            if i==0:
                prev=char
                count=int(count)+1
            
            elif char==prev:
                count=int(count)+1
               
            else:
                chars[left]=prev
                prev=char
                left+=1
                if count>1:
                    count=str(count)
                    for i in range(len(count)):
                        chars[left]=count[i]
                        left+=1
                count=int(1)

        chars[left] = prev
        left += 1
        if count > 1:
            for digit in str(count):
                chars[left] = digit
                left += 1

        return left
