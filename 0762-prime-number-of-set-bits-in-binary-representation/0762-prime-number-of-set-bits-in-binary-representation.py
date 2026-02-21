class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
         primes = {2, 3, 5, 7, 11, 13, 17, 19} 
         count =0 
         for i in range (left,  right+1 ) : 
            setbits = bin (i).count ('1')
            if setbits in primes : 
                count += 1 
         return count 