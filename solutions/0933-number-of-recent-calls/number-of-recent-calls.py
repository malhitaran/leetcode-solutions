# Number of Recent Calls (Easy)
# https://leetcode.com/problems/number-of-recent-calls/
# Accepted 2026-03-09 — Python3, runtime 8166 ms, memory 25.4 MB
class RecentCounter:

    def __init__(self):
        self.counter = []

    def ping(self, t: int) -> int:
        self.counter.append(t)  # Include the new request first

        # Count only requests in the last 3000 ms
        result = 0
        for count in self.counter:
            if count >= t - 3000:
                result += 1

        return result  # Return current count, not a list of previous counts


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
