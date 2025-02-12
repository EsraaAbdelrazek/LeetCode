class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Step 1: Apply operations
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        #step 2 
        not_zero = 0  

        for i in range(len(nums)):  
            if nums[i] != 0:
                nums[not_zero], nums[i] = nums[i], nums[not_zero] 
                not_zero += 1 

        return nums
    