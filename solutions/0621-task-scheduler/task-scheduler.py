# Task Scheduler (Medium)
# https://leetcode.com/problems/task-scheduler/
# Accepted 2026-07-11 — Python3, runtime 120 ms, memory 21.5 MB

from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''


        count


        a 3 

        b 3

        2

        a b


        ab

        for n 3

        a b 



        while there is elements in the list

            for n 

                if it exists then take that off add to output

                else add idle

            A 3
            B 3
            2


        '''
        
        letterCount=Counter(tasks)

        heap=[]
        temp=[]

        output=[]
        for letter, count in letterCount.items():
            heapq.heappush(heap, (-count, letter))


        
        while heap:

            temp=[]
            
            
            for i in range(n+1):
                
                if not heap and not temp:
                    break
                    
                
                if heap:
                    count, letter = heapq.heappop(heap)

                    count += 1
                    output.append(letter)

                    if count < 0:
                        temp.append((count, letter))
                else:
                    output.append('')

                
            for i in range(len(temp)):
                heapq.heappush(heap, (temp[i]))

        return len(output)
