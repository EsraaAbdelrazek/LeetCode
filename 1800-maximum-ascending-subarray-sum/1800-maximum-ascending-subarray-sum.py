class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # Initialize max_sum and current sum with the first element
        max_sum = curr_sum = nums[0]
        
        # Iterate through the array from the second element
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:  # Continue ascending subarray
                curr_sum += nums[i]
            else:  # Reset sum for new subarray
                curr_sum = nums[i]
            
            # Update the maximum sum found so far
            max_sum = max(max_sum, curr_sum)
        
        return max_sum
