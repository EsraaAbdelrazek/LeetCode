class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # n = len(nums)
        # expected_sum = n * (n + 1) // 2
        # actual_sum = sum(nums)
        # return expected_sum - actual_sum
        
            n = len(nums)
            xor_result = n  # Start with n because the range is [0, n]
            
            for i in range(n):
                xor_result ^= i ^ nums[i]  # XOR current index and corresponding number in array
                
            return xor_result




        