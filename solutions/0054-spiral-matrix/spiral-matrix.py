# Spiral Matrix (Medium)
# https://leetcode.com/problems/spiral-matrix/
# Accepted 2026-07-08 — Python3, runtime 0 ms, memory 19.4 MB
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:


        '''

        we go right most
        then down most
        then left most
        then up most

        we do this whilst theres nodes we havent explored, so while our set len is not the the len of all our items



        so we have a loop 

        while our set len is not the the len of all our items

        then we try go right most so a while then we go right and in range

        while then we go down whilst theres elements in teh thing and were in range

        then left most while in set and in range

        then up most while in set and in range 
        '''

        left, right=0, len(matrix[0])
        top, bottom=0, len(matrix)

        res=[]
        while left<right and top<bottom:


            #move right

            for i in range(left, right):
                res.append(matrix[top][i])
            top+=1


            #move down
            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right-=1

            if not (left<right and top<bottom):
                break

            #move left
            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])
            bottom-=1

            #move up
            for i in range(bottom-1, top-1,-1):
                res.append(matrix[i][left])
            left+=1

        return res
