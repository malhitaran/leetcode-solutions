# Largest Rectangle in Histogram (Hard)
# https://leetcode.com/problems/largest-rectangle-in-histogram/
# Accepted 2026-06-20 — Python3, runtime 119 ms, memory 36.5 MB
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # holds (start_index, height)
        output = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                output = max(output, height * (i - idx))
                start = idx  # this bar can extend back to where the popped one began
            stack.append((start, h))

        # leftover bars run all the way to the end
        for idx, height in stack:
            output = max(output, height * (len(heights) - idx))

        return output
