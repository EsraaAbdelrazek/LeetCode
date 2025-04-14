class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Time: O(1)
        # Space: O(1)

        # bitShortner is used to simulate 32-bit integer overflow
        bitShortner = 0xffffffff

        while (b & bitShortner) > 0:
            carry = (a & b) << 1     # Step 1: Find carry
            a = (a ^ b)              # Step 2: Sum without carry
            b = carry                # Step 3: Repeat with carry
        return (a & bitShortner) if b > 0 else a
