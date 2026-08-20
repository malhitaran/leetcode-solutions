# Kth Smallest Element in a BST (Medium)
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Accepted 2026-08-20 — Python3, runtime 1 ms, memory 22.2 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        save=root.val
        curr=0
        def dfs(node):
            nonlocal curr,save
            if not node:
                return

            dfs(node.left)
            curr+=1
            if curr==k:
                save=node.val
        
            dfs(node.right)
            
            
        dfs(root)
        return save
