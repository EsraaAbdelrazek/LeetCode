class Solution:

    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        total = 0
        for i in range(len(nums)):
            if bin(i).count('1') == k:
                total += nums[i]
        return total

                
      

        