# Binary Tree Right Side View (Medium)
# https://leetcode.com/problems/binary-tree-right-side-view/
# Accepted 2026-06-11 — Python3, runtime 0 ms, memory 19.2 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        q = deque([root])
        if root==None:
            return output


        while q:
            output.append(q[-1].val)
            length = len(q)
            for i in range(length):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return output
