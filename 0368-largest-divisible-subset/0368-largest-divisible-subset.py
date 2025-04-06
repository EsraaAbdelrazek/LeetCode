from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()  # Step 1: Sort the numbers
        n = len(nums)

        # Step 2: Initialize DP and parent arrays
        dp = [1] * n  # dp[i] will hold the length of the largest subset ending with nums[i]
        parent = [-1] * n  # parent[i] will track the previous index in the subset chain

        max_len = 1
        max_index = 0

        # Step 3: Build the DP and parent arrays
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j

            # Update max subset length and its index
            if dp[i] > max_len:
                max_len = dp[i]
                max_index = i

        # Step 4: Reconstruct the largest divisible subset
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = parent[max_index]

        return result[::-1]  # Reverse to get subset in increasing order
