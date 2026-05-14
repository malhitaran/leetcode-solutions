# Lowest Common Ancestor of a Binary Tree (Medium)
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Accepted 2026-05-14 — Python3, runtime 56 ms, memory 24.3 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def DFS(node):

            if not node:
                return None

            if node in (p,q):
                return node
            
            left=DFS(node.left)
            right=DFS(node.right)

            if left and right:
                return node
            
            else:
                return left or right

        return DFS(root)



'''
        if found is false dont change ancestor
        if found is true then every time we go back we need to change ancestor

        when we backtrack we find a new lowest common ancestor
        so say we had 0 and 7 

        we need to keep track of update ancestor

            3

    5                  1


6       2           0       8


     7       4

'''
