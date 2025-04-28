from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        total = 0
        curr_sum = 0

        for right in range(n):
            curr_sum += nums[right]

            while curr_sum * (right - left + 1) >= k:
                curr_sum -= nums[left]
                left += 1

            total += (right - left + 1)

        return total
