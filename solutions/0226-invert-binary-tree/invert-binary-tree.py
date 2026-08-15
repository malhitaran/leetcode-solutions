# Invert Binary Tree (Easy)
# https://leetcode.com/problems/invert-binary-tree/
# Accepted 2026-08-15 — Python3, runtime 0 ms, memory 19.3 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        '''

        i think that we add the right-left children to the queue and its a bfs
        '''
        if root is None:
            return

        root.left,root.right=root.right,root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
