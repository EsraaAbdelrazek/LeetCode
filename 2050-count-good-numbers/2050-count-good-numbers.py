class Solution:
    
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        even_choices = 5
    
        prime_choices = 4

        even_exponent = n // 2 + (n % 2)

        prime_exponent = n // 2
        
        
        even_part = pow(even_choices, even_exponent, MOD)

        prime_part = pow(prime_choices, prime_exponent, MOD)
        

        return (even_part * prime_part) % MOD
        