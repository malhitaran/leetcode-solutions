# Path Sum III (Medium)
# https://leetcode.com/problems/path-sum-iii/
# Accepted 2026-05-14 — Python3, runtime 465 ms, memory 19.8 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        '''

        2 functions 

        1 for counting from every node
        1 to give every node
        '''


        def current_sum(node, curSum):


            count=0
            if not node:
                return 0
            
            curSum+=node.val

            if curSum==targetSum:
                count+=1
            
            count+=current_sum(node.left, curSum)
            count+=current_sum(node.right, curSum)

            return count

        def every_node(node):

            if not node:
                return 0

            total=0

            total+=current_sum(node, 0)

            total+=every_node(node.left)
            total+=every_node(node.right)

            return total

        return every_node(root)
