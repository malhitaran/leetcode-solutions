# Course Schedule (Medium)
# https://leetcode.com/problems/course-schedule/
# Accepted 2026-07-05 — Python3, runtime 780 ms, memory 20.5 MB
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        '''
        2

        [[9,5], [8,7],, [5,7], [6,5],[9,5],[9,5],[9,5],]


        maybe a breadth first search

        we go through this array 


        and we do a traversal num course times

        '''
        leadsTo=defaultdict(list)

        for first, second in prerequisites:
            leadsTo[second].append(first)

        
        print(leadsTo)
        

        def dfs(second):

            q=collections.deque([second])

            while q:

                x=q.popleft()
                for number in leadsTo[x]:
                    if number==second:
                        return False
                    if number not in visited:
                        visited.add(number)
                        q.append(number)
            return True


            

            


        for node in range(numCourses): 

            visited=set()
            if dfs(node)==False:
                return False
        
        return True
