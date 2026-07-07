# Rotting Oranges (Medium)
# https://leetcode.com/problems/rotting-oranges/
# Accepted 2026-07-07 — Python3, runtime 8 ms, memory 19.3 MB
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        '''
        we can go through each position

        then do a bfs and add the adjacent

        we can turn oranges to a 2

        then we can do one final check and check if theres any 1s left

        '''

        rows, cols=len(grid), len(grid[0])

        visited=set()
        minutes=0
        q=collections.deque()
  
        def bfs(q):
            
            nonlocal minutes
            
            
            
            directions=[[-1,0],[1,0],[0,1],[0,-1]]

            while q:
                for i in range(len(q)):
                    r, c=q.popleft()
                    for ro, co in directions:
                        if r+ro in range(rows) and c+co in range(cols) and (r+ro, c+co) not in visited and grid[r+ro][c+co]==1:
                            q.append((r+ro, c+co))
                            grid[r+ro][c+co]=2
                            visited.add((r+ro, c+co))
                if q:
                    minutes+=1
                


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2 and (r, c) not in visited:
                    q.append((r,c))
                    visited.add((r,c))
        
        bfs(q)

        

        '''
        final check
        '''

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    return -1

        return minutes
