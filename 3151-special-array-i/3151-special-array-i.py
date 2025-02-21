from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
       
        for j in range(len(nums) - 1):
            if (nums[j] % 2) == (nums[j + 1] % 2): 
                return False
        return True