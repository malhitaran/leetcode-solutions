# Path Sum III (Medium)
# https://leetcode.com/problems/path-sum-iii/
# Accepted 2026-05-14 — Python3, runtime 3 ms, memory 20.6 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.paths=0
        self.pathSums= defaultdict(int)
        self.pathSums[0]=1

        def DFS(node, currSum):

            if not node:
                return
            currSum+=node.val
            self.paths+=self.pathSums[currSum-targetSum]
            self.pathSums[currSum]+=1
            
            if node.left:
                DFS(node.left, currSum)
            if node.right:
                DFS(node.right, currSum)

            self.pathSums[currSum]-=1

        DFS(root, 0)
        return self.paths
        '''

        next solution is path sums

        so we store a running count of the total
        we can subtract the target and see if a previous path sum equates to the difference

        then we know we cna remove that path and get the solution
        so we increase our path sum

        '''
