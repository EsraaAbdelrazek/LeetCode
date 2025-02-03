class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        inc, dec = 1, 1  # Track increasing and decreasing subarrays
        max_length = 1    # At minimum, a single element is a valid subarray

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
                dec = 1  # Reset decreasing count
            elif nums[i] < nums[i - 1]:
                dec += 1
                inc = 1  # Reset increasing count
            else:
                inc = dec = 1  # Reset both counts if elements are equal

            max_length = max(max_length, inc, dec)

        return max_length
