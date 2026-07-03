# Product of Array Except Self (Medium)
# https://leetcode.com/problems/product-of-array-except-self/
# Accepted 2026-07-03 — Python3, runtime 39 ms, memory 27.6 MB
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        '''

        [1, 1, 2, 6]

        [24,12,4,1]


        '''

        #wed have a prefix
        prefixArray=[0]*len(nums)

        for i, num in enumerate(nums):

            if i==0:
                count=num
                prefixArray[i]=1
            else:
                prefixArray[i]=count
                count*=num
       





        #and a suffix
        suffixArray=[0]*len(nums)

        for i in range(len(nums)-1, -1, -1):

           
            if i==len(nums)-1:
                
                suffixArray[i]=1
                count=nums[i]
                
            else:
                suffixArray[i]=count
                count*=nums[i]

        output=[]

        print(prefixArray)
        print(suffixArray)
        
        for i in range(len(prefixArray)):
            output.append(prefixArray[i]*suffixArray[i])
       
        return output
