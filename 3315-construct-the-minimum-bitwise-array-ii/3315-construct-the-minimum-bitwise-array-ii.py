class Solution:
    def minBitwiseArray(self, nums):
        N = len(nums)
        Ans = [-1] * N

        for i in range(N):
            if nums[i] == 2:
                continue

            n = nums[i]
            pos = 0

            while n > 0 and ((n >> pos) & 1) == 1:
                pos += 1

            if (1 << pos) > n:
                highestBit = n.bit_length() - 1
                n = n & ~(1 << highestBit)
            else:
                n = n & ~(1 << (pos - 1))

            Ans[i] = n

        return Ans