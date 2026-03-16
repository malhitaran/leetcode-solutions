# Count Good Nodes in Binary Tree (Medium)
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Accepted 2026-03-16 — Python3, runtime 146 ms, memory 32.2 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def good(node,listNode):
            if node is None:
                return
            if not listNode or node.val>=max(listNode):
                goodList.append(node.val)
            
            listNode.append(node.val)

            good(node.left, listNode)
            good(node.right, listNode)

            listNode.pop()
        
        listNode=[]
        goodList=[]
        good(root, listNode)
        return len(goodList)
