# My Calendar I (Medium)
# https://leetcode.com/problems/my-calendar-i/
# Accepted 2026-09-12 — Python3, runtime 215 ms, memory 20.1 MB
class MyCalendar:

    def __init__(self):
        self.bookings=[]

    def book(self, startTime: int, endTime: int) -> bool:
        
        for st, ed in self.bookings:
            if startTime < ed and st < endTime:
                return False
        self.bookings.append((startTime, endTime))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
