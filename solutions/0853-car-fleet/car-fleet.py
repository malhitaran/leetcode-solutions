# Car Fleet (Medium)
# https://leetcode.com/problems/car-fleet/
# Accepted 2026-06-19 — Python3, runtime 419 ms, memory 44.8 MB
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        '''
        first we need to get them ordered by positions

        Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]

        step one get this
        [(0,1), (3,3), (5,1), (8,4), (10,3)]
        '''
        ourL=[]
        stack=[]
        for i in range(len(position)):
            iterations=(target-position[i])/speed[i]
            ourL.append([position[i], speed[i], iterations])
        ourL.sort()

        for i in range(len(ourL)):
            
            while stack and ourL[i][1]<stack[-1][1] and ourL[i][2]>=stack[-1][2]:
                stack.pop()
                

            stack.append(ourL[i])

        return len(stack)
