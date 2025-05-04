class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        right = sum (nums) 
        left , res  = 0 , 0 
        for i in range (len (nums)-1) : 
            right -= nums[i] 
            left += nums [i] 

            res += 1 if left >= right else 0

        return res 


        