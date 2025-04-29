from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        count = 0
        left = 0
        max_count = 0

        for right in range(len(nums)):
            if nums[right] == max_val:
                max_count += 1

            # Shrink window until max_count < k
            while max_count >= k:
                if nums[left] == max_val:
                    max_count -= 1
                left += 1

            # All subarrays starting before 'left' and ending at 'right' are valid
            count += left

        return count
