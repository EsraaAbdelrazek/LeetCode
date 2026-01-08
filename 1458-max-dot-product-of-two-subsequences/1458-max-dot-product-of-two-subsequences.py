class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        
        memo = {}

       
        def dp(i,j):

            if i == len(nums1) or j == len(nums2):
                return float("-inf") 

            if (i,j) in memo:
                return memo[(i,j)]

            take = nums1[i] * nums2[j]
            res = max(
         
                take + dp(i+1, j+1),

    
                take,

           
                dp(i+1,j),

          
                dp(i,j+1),
            )

            memo[(i,j)] = res

            return memo[(i,j)]

        return dp(0,0)