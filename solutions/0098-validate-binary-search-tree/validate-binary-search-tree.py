# Validate Binary Search Tree (Medium)
# https://leetcode.com/problems/validate-binary-search-tree/
# Accepted 2026-07-02 — Python3, runtime 0 ms, memory 20.9 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        output=[]
        def DFS(node):
            nonlocal output

            if node==None:
                return 
            DFS(node.left)
            output.append(node.val)
            DFS(node.right)
            

            return output


        ourList=DFS(root)

        top = float('-inf')
        print(ourList)
        for item in ourList:
            if item>top:
                top=item
                continue
            else:
                return False
                
        return True
