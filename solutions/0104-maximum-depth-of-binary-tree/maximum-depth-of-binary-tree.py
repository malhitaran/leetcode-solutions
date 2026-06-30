# Maximum Depth of Binary Tree (Easy)
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Accepted 2026-06-30 — Python3, runtime 0 ms, memory 20.3 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        DFS where we keep track of the count, 

        breadth first search


        '''
        if not root:
            return 0

        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))
