# Longest Common Prefix (Easy)
# https://leetcode.com/problems/longest-common-prefix/
# Accepted 2026-08-04 — Python3, runtime 3 ms, memory 19.3 MB
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        res=""

        for i in range(len(strs[0])):
            for word in strs:

                if i==len(word) or word[i]!=strs[0][i]:
                    return res

            res+=strs[0][i]
            
        return res
