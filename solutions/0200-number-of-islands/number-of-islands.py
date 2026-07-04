# Number of Islands (Medium)
# https://leetcode.com/problems/number-of-islands/
# Accepted 2026-07-04 — Python3, runtime 295 ms, memory 26.6 MB
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        rows, cols = len(grid), len(grid[0])

        visit=set()
                
        islands=0


        def bfs(r, c):
            visit.add((r, c))
            q=collections.deque()
            q.append((r,c))
            directions=[[-1, 0],[1, 0],[0, 1],[0, -1]]
            while q:
                r,c=q.popleft()
                for dr, cr in directions:
                    if r+dr in range(rows) and c+cr in range(cols) and (r+dr, c+cr) not in visit and grid[r+dr][c+cr]=='1':
                        q.append((r+dr, c+cr))
                        visit.add((r+dr, c+cr))



        for r in range(rows):
            for c in range(cols):

                if grid[r][c]=='1' and (r, c) not in visit:
                    islands+=1
                    bfs(r,c)

        return islands
