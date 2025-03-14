class Solution:
    def reverseBits(self, n: int) -> int:
        binary_str = bin(n)[2:].zfill(32)   # Convert to binary and pad to 32 bits
        reversed_str = binary_str[::-1]    # Reverse the string
        return int(reversed_str, 2)        # Convert back to integer
        