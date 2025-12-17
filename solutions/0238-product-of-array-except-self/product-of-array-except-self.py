# Product of Array Except Self (Medium)
# https://leetcode.com/problems/product-of-array-except-self/
# Accepted 2025-12-17 — Python3, runtime 21 ms, memory 23.2 MB
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        # prefix products
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
