# Insert Delete GetRandom O(1) (Medium)
# https://leetcode.com/problems/insert-delete-getrandom-o1/
# Accepted 2026-10-31 — Python3, runtime 485 ms, memory 57.4 MB
import random

class RandomizedSet:

    def __init__(self):
        self.ran_set=set()

    def insert(self, val: int) -> bool:
        if val not in self.ran_set:
            self.ran_set.add(val)
            return True
        else:
            return False
       
    def remove(self, val: int) -> bool:
        if val in self.ran_set:
            self.ran_set.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.ran_set))



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
