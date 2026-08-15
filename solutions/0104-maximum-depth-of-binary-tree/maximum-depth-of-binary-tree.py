# Maximum Depth of Binary Tree (Easy)
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Accepted 2026-08-15 — Python3, runtime 2 ms, memory 22.5 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        best=0
        
        def DFS(count, node):
            nonlocal best
            if node is None:
                return 0
            if count>best:
                best=count

            DFS(count+1, node.left)
            DFS(count+1, node.right)

            return best
        

        return DFS(1, root)
