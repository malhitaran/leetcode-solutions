# Max Number of K-Sum Pairs (Medium)
# https://leetcode.com/problems/max-number-of-k-sum-pairs/
# Accepted 2026-05-18 — Python3, runtime 456 ms, memory 31.4 MB
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        '''

        [1,2,3,4]

        3 cases
        front and back equal both move in
        front and back is less move the less back/foward
        opposite of above
        '''

        [1,3,3,3,4]


        front=0
        back=len(nums)-1
        ops=0

        nums.sort()
        while front<back:
            if nums[front]+nums[back]==k:
                ops+=1
                back-=1
                front+=1
            elif nums[front]+nums[back]<k:
                front+=1
            elif nums[front]+nums[back]>k:
                back-=1
            
        return ops
