# Count Good Nodes in Binary Tree (Medium)
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Accepted 2026-07-06 — Python3, runtime 139 ms, memory 31.8 MB
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0
            good = 1 if node.val >= max_so_far else 0
            new_max = max(max_so_far, node.val)
            return good + dfs(node.left, new_max) + dfs(node.right, new_max)

        return dfs(root, float('-inf'))
