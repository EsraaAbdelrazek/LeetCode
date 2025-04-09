class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if any(x < k for x in nums):
            return -1
        print(set(x for x in nums if x>k))
        return len(set(x for x in nums if x>k))