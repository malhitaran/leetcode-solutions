# String Compression (Medium)
# https://leetcode.com/problems/string-compression/
# Accepted 2026-02-05 — Python3, runtime 4 ms, memory 19.4 MB
class Solution:
    def compress(self, chars: List[str]) -> int:
        newArray = []
        count = 1

        for i in range(len(chars) - 1):
            if chars[i] != chars[i + 1]:
                newArray.append(chars[i])
                if count > 1:
                    newArray.extend(list(str(count)))  # split digits
                    count = 1
            else:
                count += 1

        # flush the last group
        newArray.append(chars[-1])
        if count > 1:
            newArray.extend(list(str(count)))  # split digits

        # write back into chars
        chars[:len(newArray)] = newArray
        return len(newArray)
