class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len (nums) 
        goal = n-1 

        for i in range (n-1 , -1  , -1 ): 
            maxJump = nums[i] 
            if i + maxJump >= goal : 
                goal = i 


        return goal ==0 
        