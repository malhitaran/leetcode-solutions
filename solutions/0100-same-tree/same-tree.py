# Same Tree (Easy)
# https://leetcode.com/problems/same-tree/
# Accepted 2026-06-30 — Python3, runtime 0 ms, memory 19.3 MB
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:


        queue1=deque([p])
        queue2=deque([q])

    

        while queue1 and queue2:
            x=queue1.popleft()
            y=queue2.popleft()

            if x==None and y!=None or y==None and x!=None:
                return False

            if x and y and x.val!=y.val:
                print('yes')
                return False
            
            if x and y:
                queue1.append(x.left)
                queue1.append(x.right)
                queue2.append(y.left)
                queue2.append(y.right)
            


        if queue1 or queue2:
            return False
        return True
