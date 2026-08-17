# Number of Islands (Medium)
# https://leetcode.com/problems/number-of-islands/
# Accepted 2026-08-17 — Python3, runtime 389 ms, memory 27.2 MB
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        '''


        '''
        
        rows,cols=len(grid), len(grid[0])
        seen=set()
        islands=0
        def bfs(r,c):
            queue=deque([(r,c)])
            directions=[[1,0],[0,1],[-1,0],[0,-1]]
            while queue:
                print(queue)
                r,c=queue.popleft()
                for rp, cp in directions:
                    if (r+rp in range(rows)) and (c+cp in range(cols)) and ((r+rp,c+cp) not in seen) and grid[r+rp][c+cp]=="1":
                        seen.add((r+rp,c+cp))
                        queue.append((r+rp,c+cp))
                        


        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=="0":
                    continue
                if (row, col) in seen:
                    continue
                islands+=1
                seen.add((row,col))
                bfs(row,col)

        return islands
