# Rotting Oranges (Medium)
# https://leetcode.com/problems/rotting-oranges/
# Accepted 2026-08-31 — Python3, runtime 7 ms, memory 19.5 MB
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols=len(grid),len(grid[0])
        seen=set()
        def bfs(queue):
            minutes=0
            directions=[[1,0],[-1,0],[0,1],[0,-1]]
            while queue:
                for i in range(len(queue)):
                    r,c=queue.popleft()
                    for ro, co in directions:
                        if (r+ro<rows and r+ro>=0) and (c+co<cols and c+co>=0) and (r+ro,c+co) not in seen and grid[r+ro][c+co]==1:
                            grid[r+ro][c+co]=2
                            queue.append((r+ro,c+co))
                            seen.add((r+ro,c+co))
                if queue:
                    minutes += 1
            return minutes

        queue=collections.deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==2 and (row,col) not in seen:
                    queue.append((row, col))

        
        m=bfs(queue)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    return -1

        return m
