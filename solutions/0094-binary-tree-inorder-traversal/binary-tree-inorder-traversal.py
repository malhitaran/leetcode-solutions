# Binary Tree Inorder Traversal (Easy)
# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Accepted 2026-08-23 — Python3, runtime 0 ms, memory 19.3 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res=[]
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        
        return (
            self.inorderTraversal(root.left)
            + [root.val]
            +self.inorderTraversal(root.right)
        )
