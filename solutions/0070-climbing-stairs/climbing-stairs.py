# Climbing Stairs (Easy)
# https://leetcode.com/problems/climbing-stairs/
# Accepted 2026-10-31 — Python3, runtime 0 ms, memory 19.4 MB
class Solution:
    def climbStairs(self, n: int) -> int:
        '''

            dfs
            -were recalcualting the same paths again and again
        '''
        seen=defaultdict(int)
 
        def dfs(cnt):

            if cnt==n:
                return 1
            if cnt>n:
                return 0
            
            if cnt in seen:
                return seen[cnt]
            
            seen[cnt]=dfs(cnt+1) + dfs(cnt + 2)
            return seen[cnt]
        
        return dfs(0)
