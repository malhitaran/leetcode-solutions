# Count Good Nodes in Binary Tree (Medium)
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Accepted 2026-08-23 — Python3, runtime 135 ms, memory 32 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res=0
        def dfs(node, curr):
            nonlocal res
            if not node:
                return
            if node.val>=curr:
                res+=1
                curr=node.val
            dfs(node.left,curr)
            dfs(node.right,curr)
        dfs(root, float('-inf'))
        return res
