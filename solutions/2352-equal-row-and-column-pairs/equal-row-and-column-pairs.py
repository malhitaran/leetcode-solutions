# Equal Row and Column Pairs (Medium)
# https://leetcode.com/problems/equal-row-and-column-pairs/
# Accepted 2026-08-07 — Python3, runtime 18 ms, memory 24.8 MB
from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        row_freq = Counter(tuple(row) for row in grid)

        output = 0

        for c in range(cols):
            temp = []

            for r in range(rows):
                temp.append(grid[r][c])

            output += row_freq[tuple(temp)]

        return output
