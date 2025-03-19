from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_value = nums[0]
        max_diff = -1

        for j in range(1, len(nums)):
            if nums[j] > min_value:
                max_diff = max(max_diff, nums[j] - min_value)
            else:
                min_value = nums[j]
        
        return max_diff
