class Solution:
    def rob(self, nums: List[int]) -> int:
       
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]

            prev2, prev1 = 0, 0  # Represents dp[i-2] and dp[i-1]
            
            for num in nums:
                new_rob = max(prev1, num + prev2)  # max of skipping or robbing current house
                prev2, prev1 = prev1, new_rob  # Shift values forward
            
            return prev1  # The maximum money that can be robbed

        