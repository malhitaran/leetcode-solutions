# Symmetric Tree (Easy)
# https://leetcode.com/problems/symmetric-tree/
# Accepted 2026-07-04 — Python3, runtime 0 ms, memory 19.5 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:


        '''

        if the left branch is equal to the right branch and the right branch is equal to the left branch


        '''
        output1=[]
        def DFS1(node):

            if node==None:
                output1.append(None)
                return

            output1.append(node.val)

            DFS1(node.left)
            DFS1(node.right)

        output2=[]
        def DFS2(node):

            if node==None:
                output2.append(None)
                return
            output2.append(node.val)

            DFS2(node.right)
            DFS2(node.left)
            
        DFS1(root)
        DFS2(root)

        return output1==output2
