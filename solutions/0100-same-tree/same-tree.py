# Same Tree (Easy)
# https://leetcode.com/problems/same-tree/
# Accepted 2026-08-19 — Python3, runtime 0 ms, memory 19.3 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        res=True
        def dfs(p,q):
            nonlocal res
            if not p and not q:
                return
            if not p or not q:
                res=False
                return
            if p.val!=q.val:
                res=False
                return
            dfs(p.left,q.left)
            dfs(p.right,q.right)

        dfs(p,q)
        return res
