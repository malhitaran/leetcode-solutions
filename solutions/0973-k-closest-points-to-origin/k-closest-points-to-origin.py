# K Closest Points to Origin (Medium)
# https://leetcode.com/problems/k-closest-points-to-origin/
# Accepted 2026-06-12 — Python3, runtime 19 ms, memory 23.9 MB
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        

        
        '''

        [[1,3],[-2,2]]

        for all items find eculidian        n


        store as index and eculidian value pair

        sort that dictionary    nlogn

        take k items of that and output

        sortedList=sorted(ourDict.items(), key=lambda x:x[1])

        output=sortedList.keys()
        '''
        points.sort(key=lambda x: x[0]**2 + x[1]**2)
        

        
        return points[:k]
