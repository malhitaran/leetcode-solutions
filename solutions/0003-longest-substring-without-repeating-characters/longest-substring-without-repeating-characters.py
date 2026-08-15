# Longest Substring Without Repeating Characters (Medium)
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Accepted 2026-08-15 — Python3, runtime 271 ms, memory 19.9 MB
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,best=0,0

        seen=collections.defaultdict(int)

        for r in range(len(s)):

            seen[s[r]]+=1

            while seen[s[r]]>1:
                seen[s[l]]-=1
                l+=1
            
            best=max(best, r-l+1)

        return best
