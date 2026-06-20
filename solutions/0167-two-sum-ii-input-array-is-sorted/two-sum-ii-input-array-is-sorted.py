# Two Sum II - Input Array Is Sorted (Medium)
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Accepted 2026-06-20 — Python3, runtime 9 ms, memory 20.5 MB
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        start=0
        back=len(numbers)-1


        while start<back:
            x=numbers[start]+numbers[back]

            if x==target:
                return [start+1,back+1]
            if x>target:
                back-=1
            else:
                start+=1
