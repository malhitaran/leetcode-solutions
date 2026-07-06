# Binary Tree Right Side View (Medium)
# https://leetcode.com/problems/binary-tree-right-side-view/
# Accepted 2026-07-06 — Python3, runtime 0 ms, memory 19.5 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        

        '''

        bfs
        where we add the right node, if there is no right now we 


        we want to prioritise right


        push right then left

        then we keep pushing right to the front

        stack data structure

        3, 2, 2
        '''
        if root:
            res=[root.val]
        else:
            return []
        depth=0

        def dfs(node, current):
            nonlocal depth
            if node==None:
                return

            if current>depth:
                depth=current
                res.append(node.val)

            dfs(node.right, current+1)
            dfs(node.left, current+1)

        dfs(root, depth)

        return res
