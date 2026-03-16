# Count Good Nodes in Binary Tree (Medium)
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Accepted 2026-03-16 — Python3, runtime 128 ms, memory 32 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxVal):
            if node is None:
                return 0

            # Is this node good?
            good = 1 if node.val >= maxVal else 0

            # Update maxVal for children
            maxVal = max(maxVal, node.val)

            # Recursively count good nodes in left and right
            return good + dfs(node.left, maxVal) + dfs(node.right, maxVal)

        return dfs(root, root.val)
