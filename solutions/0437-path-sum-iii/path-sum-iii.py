# Path Sum III (Medium)
# https://leetcode.com/problems/path-sum-iii/
# Accepted 2026-08-18 — Python3, runtime 7 ms, memory 20.5 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        '''
        wed store the sum of the path up to that point 


        '''
        paths=0
        seen=defaultdict(int)
        seen[0]=1
        def dfs(node,currSum):
            nonlocal paths
            if not node:
                return
            currSum+=node.val
            paths+=seen[currSum-targetSum]

            seen[currSum]+=1

            dfs(node.left, currSum)
            dfs(node.right, currSum)
            seen[currSum]-=1

        dfs(root, 0)
        return paths
