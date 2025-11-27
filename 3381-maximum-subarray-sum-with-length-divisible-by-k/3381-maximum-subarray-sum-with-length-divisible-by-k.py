from typing import List

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        INF = 4 * 10**18
        
        minPref = [INF] * k
        
        prefix = 0
        ans = -INF
        
        minPref[0] = 0
        
        for i, val in enumerate(nums):
            prefix += val
            rem = (i + 1) % k
            
            if minPref[rem] != INF:
                ans = max(ans, prefix - minPref[rem])
            
            if prefix < minPref[rem]:
                minPref[rem] = prefix
        
        return ans