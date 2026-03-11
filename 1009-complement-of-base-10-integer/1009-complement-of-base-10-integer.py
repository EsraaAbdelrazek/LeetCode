class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        
        ans = 0
        bit = 1

        while n > 0:
            if not (n & 1):
                ans |= bit

            bit <<= 1
            n >>= 1

        return ans