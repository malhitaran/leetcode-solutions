# Flood Fill (Easy)
# https://leetcode.com/problems/flood-fill/
# Accepted 2026-07-04 — Python3, runtime 4 ms, memory 19.3 MB
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        

        rows, cols=len(image), len(image[0])

        visited=set()

        ourColour=image[sr][sc]
        image[sr][sc]=color

        
        def bfs(sr, sc):
            nonlocal ourColour
            visited.add((sr, sc))
            
            q=collections.deque()
            q.append((sr, sc))
            directions=[[-1, 0], [1, 0], [0, -1], [0, 1]]

            while q:
                sr, sc=q.popleft()
                for r, c in directions:

                    if sr+r in range(rows) and sc+c in range(cols) and (sr+r, sc+c) not in visited and image[sr+r][sc+c]==ourColour:
                        image[sr+r][sc+c]=color
                        q.append((sr+r, sc+c))
                        visited.add((sr+r, sc+c))
            

        bfs(sr, sc)
        return image
