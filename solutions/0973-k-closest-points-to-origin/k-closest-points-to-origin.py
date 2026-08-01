# K Closest Points to Origin (Medium)
# https://leetcode.com/problems/k-closest-points-to-origin/
# Accepted 2026-08-01 — Python3, runtime 58 ms, memory 25.7 MB
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        '''

        for each of these coordinates, i can put it into a tuple then add the distance in the first part of teh tuple, then the coordinates

        '''

        heap=[]
        res=[]
        for x,y in points:
            dis=x**2 + y**2
            heap.append((dis, x, y))

        heapq.heapify(heap)
        
        for i in range(k):
            x=heapq.heappop(heap)
            res.append([x[1],x[2]])


        return res
