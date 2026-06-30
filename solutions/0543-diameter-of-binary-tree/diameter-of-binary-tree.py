# Diameter of Binary Tree (Easy)
# https://leetcode.com/problems/diameter-of-binary-tree/
# Accepted 2026-06-30 — Python3, runtime 4 ms, memory 22.2 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        '''
        the pattern is the max distance between left and the right

        '''
        res=0

        def DFS(node):
            nonlocal res
            if node==None:
                return 0

            left=DFS(node.left)
            right=DFS(node.right)
            res=max(res,left+right)

            return 1+max(left, right)

        DFS(root)
            
        return res
