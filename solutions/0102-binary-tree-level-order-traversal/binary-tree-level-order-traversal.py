# Binary Tree Level Order Traversal (Medium)
# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Accepted 2026-07-02 — Python3, runtime 0 ms, memory 19.9 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:


        output=[]

        queue=deque([root])

        

        while queue:
            iterations=len(queue)

            temp=[]

            for i in range(iterations):
                element=queue.popleft()

                if element:
                    temp.append(element.val)
                    queue.append(element.left)
                    queue.append(element.right)
                    
            if temp:
                output.append(temp)

        return output
