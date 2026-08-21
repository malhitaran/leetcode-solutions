# Number of Islands (Medium)
# https://leetcode.com/problems/number-of-islands/
# Accepted 2026-08-21 — Python3, runtime 281 ms, memory 21.6 MB
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows,cols=len(grid),len(grid[0])
        islands=0

        def bfs(row,col):
            queue=deque([(row,col)])
            directions=[[1,0],[-1,0],[0,1],[0,-1]]
            while queue:
                r,c=queue.popleft()
                for ro,co in directions:
                    if (r+ro in range(rows)) and (c+co in range(cols)) and (grid[r+ro][c+co]=="1"):
                        grid[r+ro][c+co]="0"
                        queue.append((r+ro,c+co))
        
        for row in range(rows):
            for col in range(cols):
                if (grid[row][col]=="1"):
                    islands+=1
                    bfs(row,col)

        return islands
