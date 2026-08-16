# Leaf-Similar Trees (Easy)
# https://leetcode.com/problems/leaf-similar-trees/
# Accepted 2026-08-16 — Python3, runtime 0 ms, memory 19.3 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def DFS(node,curr):
            if node is None:
                return
            if node.left is None and node.right is None:
                curr.append(node.val)
            DFS(node.left,curr)
            DFS(node.right,curr)
            
        leaves1,leaves2=[],[]
        DFS(root1,leaves1)
        DFS(root2,leaves2)

        return leaves1==leaves2
