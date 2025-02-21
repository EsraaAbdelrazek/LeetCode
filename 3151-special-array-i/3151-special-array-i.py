from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
       
        for it in range(len(nums) - 1):
            if (nums[it] % 2) == (nums[it + 1] % 2): 
                return False
        return True