from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        not_zero = 0  

        for i in range(len(nums)):  
            if nums[i] != 0:
                nums[not_zero], nums[i] = nums[i], nums[not_zero] 
                not_zero += 1 