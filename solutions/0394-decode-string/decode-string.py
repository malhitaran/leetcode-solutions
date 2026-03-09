# Decode String (Medium)
# https://leetcode.com/problems/decode-string/
# Accepted 2026-03-09 — Python3, runtime 0 ms, memory 19.3 MB
class Solution:
    def decodeString(self, s: str) -> str:


        num_stack = []
        str_stack = []
        curr_num = 0
        curr_str = ""

        for char in s:
            if char.isdigit():
                # build the number, e.g., "12[a]"
                curr_num = curr_num * 10 + int(char)
            elif char == '[':
                # push current number and string onto stacks
                num_stack.append(curr_num)
                str_stack.append(curr_str)
                curr_num = 0
                curr_str = ""
            elif char == ']':
                # pop number and previous string, repeat current string
                repeat_times = num_stack.pop()
                prev_str = str_stack.pop()
                curr_str = prev_str + curr_str * repeat_times
            else:
                # regular character, append
                curr_str += char

        return curr_str
