# Permutation in String (Medium)
# https://leetcode.com/problems/permutation-in-string/
# Accepted 2026-08-15 — Python3, runtime 19 ms, memory 19.4 MB
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1c,s2c,l=Counter(s1),collections.defaultdict(int),0
        for r in range(len(s2)):
            if s2[r] in s1c:
                s2c[s2[r]]+=1
                while s2c[s2[r]]>s1c[s2[r]]:
                    s2c[s2[l]]-=1
                    l+=1
            else:
                s2c=defaultdict(int)
                l=r+1
            if s2c==s1c:
                return True

        return False
