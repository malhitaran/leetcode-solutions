# Invert Binary Tree (Easy)
# https://leetcode.com/problems/invert-binary-tree/
# Accepted 2026-06-30 — Python3, runtime 0 ms, memory 19.2 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        queue=deque([root])
        
        while queue:
            x=queue.popleft()
            if x!=None:
                x.left, x.right=x.right, x.left
        
                queue.append(x.left)
                queue.append(x.right)
        return root
