from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_non_decreasing(arr):
           
            for i in range(1, len(arr)):
                if arr[i] < arr[i-1]:
                    return False
            return True

        operations = 0
        
      
        while not is_non_decreasing(nums):
            min_sum = float('inf')
            min_index = -1
            
          
            for i in range(len(nums) - 1):
                if nums[i] + nums[i+1] < min_sum:
                    min_sum = nums[i] + nums[i+1]
                    min_index = i
            
           
            nums[min_index] = nums[min_index] + nums[min_index + 1]
            nums.pop(min_index + 1)  
            operations += 1
        
        return operations