class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = 0
        cur = 0  # bitmask
        l = 0

        for r in range(len(nums)):
            while cur & nums[r]:
                cur = cur ^ nums[l]
                l += 1
            res = max(res, r - l + 1)
            cur = cur ^ nums[r]
        return res
