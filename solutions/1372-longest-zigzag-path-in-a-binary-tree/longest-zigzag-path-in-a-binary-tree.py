# Longest ZigZag Path in a Binary Tree (Medium)
# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
# Accepted 2026-05-14 — Python3, runtime 40 ms, memory 38.1 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.path=0

        def DFS(node, left, curr):
            if not node:
                return
            self.path=max(self.path, curr)

            if left:
                DFS(node.right, False, curr+1)
                DFS(node.left, True, 1)
            else:
                DFS(node.right, False, 1)
                DFS(node.left, True, curr +1)
            
        DFS(root.right, False, 1)
        DFS(root.left, True, 1)

        return self.path


        '''
        2n squared solution

        first function visit every node twice(left dir/right dir)
        second function cal longest paths
        '''
