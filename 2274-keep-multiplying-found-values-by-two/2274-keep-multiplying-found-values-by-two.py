class Solution:
    def findFinalValue(self, nums: list[int], k: int) -> int:
        bits = 0
        for num in nums:
            q, r = divmod(num, k)
            if r == 0 and (q & (q - 1)) == 0:
                bits |= q
        n = bits + 1
        return k * (n & -n)
