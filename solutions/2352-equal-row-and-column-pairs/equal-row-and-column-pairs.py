# Equal Row and Column Pairs (Medium)
# https://leetcode.com/problems/equal-row-and-column-pairs/
# Accepted 2026-03-08 — Python3, runtime 24 ms, memory 24.5 MB
from collections import Counter

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n=len(grid)
        count1=Counter(tuple(row) for row in grid)
        ans=0

        for c in range(n):
            col=tuple(grid[r][c] for r in range(n))
            ans+=count1[col]
        
        return ans
