# Lowest Common Ancestor of a Binary Search Tree (Medium)
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Accepted 2026-07-01 — Python3, runtime 71 ms, memory 22.9 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        '''
        we find one node, then we try find the next node, keeping track consistently of the lca

        if the node is on the left and the other is on the right we know that the common node will be node thats the lca

        otherwise if its not found on the right return the current node
        '''

        curr=root
        
        low=min(p.val, q.val)
        high=max(p.val, q.val)

        while curr:

            if curr.val>high:
                curr=curr.left
            elif curr.val<low:
                curr=curr.right
            else:
                return curr
