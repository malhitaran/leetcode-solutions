# Permutations (Medium)
# https://leetcode.com/problems/permutations/
# Accepted 2026-08-27 — Python3, runtime 3 ms, memory 19.3 MB
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        i think we would do for loops but we would have a path list each time too

        so say for 123 we would do a for loop for 3 right 

        then we would have it so as long as teh i is not in our path list
        
        so for 1 it would recurse on 2 3, for 12 it would recurse on 3, for 13 it would recurse on 2, then wed do the next iteration in the wider for loop and move to 2


                1                   2                      3
                                            
            2       3           3       1              2       1
        
        3               2     1             3       1               2

        so it would be liek this
        so we would go through each number in the number in the list
        then start a for loop with a path list so far and recurs, so for exampel lets take the first tree

        that first tree has only [1] in its path list, so we do a for loop up to 3 because thats the len of list, then we would recurs on 2 and 3, passing in as the path list [1,2] and [1,3], same thing we would start another for loop with that path list passed in then we would do [123] and [321]

        now i got to figure out where to unwind, 
        '''
        res=[]
        def recurs(pathlist):
            if len(pathlist)==len(nums):
                res.append(list(pathlist))
                return
            for i in range(len(nums)):
                if nums[i] not in pathlist:
                    pathlist.append(nums[i])
                    recurs(pathlist)
                    pathlist.pop()

        recurs([])
        return res
