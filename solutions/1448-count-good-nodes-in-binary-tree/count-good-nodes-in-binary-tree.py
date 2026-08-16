# Count Good Nodes in Binary Tree (Medium)
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Accepted 2026-08-16 — Python3, runtime 126 ms, memory 31.8 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        '''


        '''
        curr=0
        def DFS(node,maxSeen):
            nonlocal curr
            if node is None:
                return
            
            if node.val>=maxSeen:
                maxSeen=node.val
                curr+=1
                

            DFS(node.left,maxSeen)
            DFS(node.right,maxSeen)
        
        
        DFS(root, root.val)

        return curr
