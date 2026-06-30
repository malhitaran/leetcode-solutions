# Maximum Depth of Binary Tree (Easy)
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Accepted 2026-06-30 — Python3, runtime 2 ms, memory 20.3 MB
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
        best=0
        count=0

        if root==None:
            return 0

        def DFS(node):
            nonlocal count, best
            if node==None:
                return
            count+=1
            DFS(node.left)
            DFS(node.right)
            best=max(best, count)
            count-=1

            return best
        
        return DFS(root)
