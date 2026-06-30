# Balanced Binary Tree (Easy)
# https://leetcode.com/problems/balanced-binary-tree/
# Accepted 2026-06-30 — Python3, runtime 4 ms, memory 20.3 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        ourBool=True
        def DFS(node):
            nonlocal ourBool

            if node==None:
                return 0
            left=DFS(node.left)
            right=DFS(node.right)

            if abs(left-right)>1:
                ourBool=False


            return 1+max(left, right)

        DFS(root)
        return ourBool
