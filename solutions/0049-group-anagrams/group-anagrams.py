# Group Anagrams (Medium)
# https://leetcode.com/problems/group-anagrams/
# Accepted 2026-07-03 — Python3, runtime 15 ms, memory 24 MB

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        countList=defaultdict(list)#keys will be a list[a-z]:frequency

        for i in range(len(strs)):

            count=[0]*26

            for letter in strs[i]:
                count[ord(letter)-ord('a')]+=1

            countList[tuple(count)].append(strs[i])

        return list(countList.values())
