# Maximum Depth of Binary Tree (Easy)
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Accepted 2026-08-15 — Python3, runtime 3 ms, memory 22.6 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0

        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))
