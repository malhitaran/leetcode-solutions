# Search a 2D Matrix (Medium)
# https://leetcode.com/problems/search-a-2d-matrix/
# Accepted 2026-06-27 — Python3, runtime 0 ms, memory 19.7 MB
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        how do we get n and m when we got index 5
     

 

        n=nums//m
        m=nums mod m -1



        '''


        end=(len(matrix[0])*len(matrix))-1
        start=0
        m=len(matrix[0])

        while start<=end:
            print(end)
            midpoint=((end-start)//2)+start
        
            x=midpoint//m
            y=(midpoint%m)
            if y<0:
                y=0

           
            if matrix[x][y]==target:
                return True
            elif matrix[x][y]>target:
                end=midpoint-1
            else:
                start=midpoint+1
                print(start)
        return False
