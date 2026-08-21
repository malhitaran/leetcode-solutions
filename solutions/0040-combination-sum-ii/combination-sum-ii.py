# Combination Sum II (Medium)
# https://leetcode.com/problems/combination-sum-ii/
# Accepted 2026-08-21 — Python3, runtime 35 ms, memory 19.5 MB
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res=[]
        candidates.sort()
        def dfs(i, cur, total):
            if total==target:
                res.append(cur.copy())
                return
            if total>=target or i>=len(candidates):
                return
            
            cur.append(candidates[i])
            dfs(i+1, cur, total+candidates[i])
            cur.pop()
            x=i
            while x + 1 < len(candidates) and candidates[x] == candidates[x + 1]:
                x += 1
            dfs(x+1, cur, total)

        dfs(0, [], 0)
        return res
