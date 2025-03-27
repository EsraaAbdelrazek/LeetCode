from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
       
        candidate, count = None, 0
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

     
        total_count = nums.count(candidate)

      
        left_count = 0
        for i in range(len(nums) - 1):
            if nums[i] == candidate:
                left_count += 1
            
            left_size = i + 1
            right_size = len(nums) - left_size
            
            if left_count * 2 > left_size and (total_count - left_count) * 2 > right_size:
                return i 
        
        return -1 
