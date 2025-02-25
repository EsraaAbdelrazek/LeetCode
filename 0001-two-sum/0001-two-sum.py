from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {} 
        length = len(nums)
        
        for i in range(length):
            complement = target - nums[i]
            if complement in num_map:
                return [num_map[complement], i] 
            num_map[nums[i]] = i 
        
        return []
