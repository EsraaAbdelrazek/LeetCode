class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sm = sum (nums)
        return (sm % k)
        