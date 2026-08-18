# Balanced Binary Tree (Easy)
# https://leetcode.com/problems/balanced-binary-tree/
# Accepted 2026-08-18 — Python3, runtime 1 ms, memory 20.4 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        '''
        max of left and right never differs by more than 1?
        '''
        res=True
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)

            if left-1>right or right-1>left:
                res=False
            

            return 1+ max(left,right)
        
        dfs(root)
        return res
