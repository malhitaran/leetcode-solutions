# Binary Tree Right Side View (Medium)
# https://leetcode.com/problems/binary-tree-right-side-view/
# Accepted 2026-06-11 — Python3, runtime 0 ms, memory 19.4 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output=[]
        height=0
        tempHeight=0

        def DFS(node, height):
            if node==None:
                return
            
            if len(output) == height:
                output.append(node.val)

            DFS(node.right,height+1)
            DFS(node.left,height+1)
            
        DFS(root,0)
        return output
