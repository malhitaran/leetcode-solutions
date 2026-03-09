# Number of Recent Calls (Easy)
# https://leetcode.com/problems/number-of-recent-calls/
# Accepted 2026-03-09 — Python3, runtime 40 ms, memory 24.7 MB
from collections import deque

class RecentCounter:

    def __init__(self):
        self.queue = deque()  # store timestamps of requests

    def ping(self, t: int) -> int:
        # add the new request
        self.queue.append(t)
        
        # remove all requests older than t - 3000
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        
        # number of requests in the last 3000 ms
        return len(self.queue)
