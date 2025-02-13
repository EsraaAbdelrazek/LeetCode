class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify (nums) 
        c = 0 
        while nums[0] < k : 
            x = heappop (nums) 
            c+= 1
        return c