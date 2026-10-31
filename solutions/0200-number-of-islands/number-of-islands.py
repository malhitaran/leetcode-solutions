# Number of Islands (Medium)
# https://leetcode.com/problems/number-of-islands/
# Accepted 2026-10-31 — Python3, runtime 253 ms, memory 21.4 MB
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        '''
        bfs

        dfs

        '''
        rows, cols=len(grid), len(grid[0])
        islands=0

        def bfs(r, c):
            directions=[[0,1], [1,0],[-1,0],[0,-1]]
            queue=collections.deque([(r, c)])
            while queue: 
                r, c = queue.popleft()
                for ro, co in directions:
                    if (0<= r+ro <rows) and (0<= c+co <cols) and grid[r+ro][c+co]=='1':
                        queue.append((r+ro, c+co))
                        grid[r+ro][c+co]='0'
                


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1':
                    bfs(r,c)
                    islands+=1
        return islands
