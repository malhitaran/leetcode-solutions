# Merge Intervals (Medium)
# https://leetcode.com/problems/merge-intervals/
# Accepted 2026-07-04 — Python3, runtime 4 ms, memory 22.5 MB
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        sort by there ending

        then we can see if the start overlaps then add it to the current list and update last element

        otherwise add it as a new element

        '''

        #sort the array 

        intervals.sort(key=lambda x:x[0])

        output=[]
        res=[]
        for interval in intervals:

            
            if output and interval[0]<=output[-1][1]:

                if interval[1]>output[-1][1]:
                    output[-1][1]=interval[1]
               

            else:
                output.append(interval)


        return output
