class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        def is_prime(num: int) -> bool:
            if num <= 1:
                return False
            if num <= 3:
                return True
            if num % 2 == 0 or num % 3 == 0:
                return False
            i = 5
            while i * i <= num:
                if num % i == 0 or num % (i + 2) == 0:
                    return False
                i += 6
            return True
        
        primes_set = set()
        n = len(s)
        
        for i in range(n):
            for j in range(i + 1, n + 1):
                sub = s[i:j]
                val = int(sub) 
                if val not in primes_set and is_prime(val):
                    primes_set.add(val)
        
        if not primes_set:
            return 0
        
        largest_primes = sorted(primes_set, reverse=True)
        return sum(largest_primes[:3])
