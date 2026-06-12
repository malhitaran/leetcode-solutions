# K Closest Points to Origin (Medium)
# https://leetcode.com/problems/k-closest-points-to-origin/
# Accepted 2026-06-12 — Python3, runtime 69 ms, memory 24.7 MB
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
        ourDict=dict()
        x=0
        for i in range(len(points)):
            x=0
            for j in range(len(points[i])):
                x+=points[i][j]**2
            ourDict[i]=x
        
        sortedDict=sorted(ourDict.items(), key=lambda x:x[1])
        output=[]
        for i in range(k):
            output.append(points[sortedDict[i][0]])
        

        
        return output
