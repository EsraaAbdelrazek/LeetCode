class Solution:
    def reverseBits(self, n: int) -> int:
        binary_n = bin (n)[2:]

        padded = binary_n .zfill (32) 

        reversed_n = padded[::-1] 
        num = int (reversed_n , 2 ) 

        return num 
        