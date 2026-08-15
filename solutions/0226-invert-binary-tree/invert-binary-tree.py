# Invert Binary Tree (Easy)
# https://leetcode.com/problems/invert-binary-tree/
# Accepted 2026-08-15 — Python3, runtime 0 ms, memory 19.4 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        '''

        i think that we add the right-left children to the queue and its a bfs
        '''

        queue=deque([root])

        while queue:
            x=queue.popleft()

            if x:
                queue.append(x.right)
                queue.append(x.left)
            
                x.left,x.right=x.right,x.left
        
        return root
