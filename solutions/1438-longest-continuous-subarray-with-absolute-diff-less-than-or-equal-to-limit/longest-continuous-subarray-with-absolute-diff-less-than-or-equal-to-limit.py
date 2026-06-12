# Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit (Medium)
# https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
# Accepted 2026-06-12 — Python3, runtime 175 ms, memory 30 MB
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        

        left = 0
        best = 0

        maxDeque = deque()  # decreasing order
        minDeque = deque()  # increasing order

        for i in range(len(nums)):
            # Add nums[i] into maxDeque
            while maxDeque and nums[i] > maxDeque[-1]:
                maxDeque.pop()
            maxDeque.append(nums[i])

            # Add nums[i] into minDeque
            while minDeque and nums[i] < minDeque[-1]:
                minDeque.pop()
            minDeque.append(nums[i])

            # Shrink window if invalid
            while maxDeque[0] - minDeque[0] > limit:
                if nums[left] == maxDeque[0]:
                    maxDeque.popleft()

                if nums[left] == minDeque[0]:
                    minDeque.popleft()

                left += 1

            best = max(best, i - left + 1)

        return best
