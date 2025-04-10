class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
    
        result = 0
        for bit in range(32):  # assuming 32-bit integers
            count = 0
            for num in nums:
                if num & (1 << bit):
                    count += 1
            if count >= k:
                result |= (1 << bit)
        return result
    