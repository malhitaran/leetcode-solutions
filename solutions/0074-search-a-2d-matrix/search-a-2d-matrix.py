# Search a 2D Matrix (Medium)
# https://leetcode.com/problems/search-a-2d-matrix/
# Accepted 2026-08-15 — Python3, runtime 0 ms, memory 19.7 MB
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       
        amount=len(matrix)*len(matrix[0])
        start,end=0,amount-1
        

        while start<=end:
            mid=(start+end)//2
            print(mid)
            r=mid//len(matrix[0])
            c=mid%len(matrix[0])
            print(r,c)
            if matrix[r][c]==target:
                return True
        
            if matrix[r][c]>target:
                end=mid-1
            else:
                start=mid+1

        return False
