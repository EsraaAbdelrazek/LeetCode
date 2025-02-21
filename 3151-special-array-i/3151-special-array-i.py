from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        """
        Check if the given array is special, meaning every adjacent pair 
        consists of one odd and one even number.
        
        :param nums: List of integers
        :return: True if the array is special, otherwise False
        """
        for i in range(len(nums) - 1):
            if (nums[i] % 2) == (nums[i + 1] % 2):  # Both even or both odd
                return False
        return True