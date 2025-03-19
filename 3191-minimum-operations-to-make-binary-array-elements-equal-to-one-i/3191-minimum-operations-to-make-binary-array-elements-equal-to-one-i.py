from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ops = 0

        for i in range(n - 2):
            if nums[i] == 0:
             
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                ops += 1

    
        if all(x == 1 for x in nums):
            return ops
        else:
            return -1
