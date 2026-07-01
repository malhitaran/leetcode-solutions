# Subtree of Another Tree (Easy)
# https://leetcode.com/problems/subtree-of-another-tree/
# Accepted 2026-07-01 — Python3, runtime 50 ms, memory 19.5 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if subRoot==None:
            return True
        if root==None:
            return False

        if self.sameTree(root,subRoot):
            return True

        return (self.isSubtree(root.left,subRoot) or
        self.isSubtree(root.right, subRoot))
        


    def sameTree(self, s,t):
        if s==None and t==None:
            return True

        if s==None or t==None:
            return False

        if s.val==t.val:
            return (self.sameTree(s.left, t.left) and
            self.sameTree(s.right, t.right))
        else: return False
