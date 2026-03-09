# Dota2 Senate (Medium)
# https://leetcode.com/problems/dota2-senate/
# Accepted 2026-03-09 — Python3, runtime 8 ms, memory 19.7 MB
from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque()
        dire = deque()
        
        # store indices of each party
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        
        # simulate rounds
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()
            
            # the senator with the smaller index bans the other
            if r < d:
                radiant.append(r + n)  # goes to back with updated index
            else:
                dire.append(d + n)
        
        return "Radiant" if radiant else "Dire"
