from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
       
        sieve = [True] * (right + 1)
        sieve[0] = sieve[1] = False  # 0 and 1 are not prime

        for num in range(2, int(right**0.5) + 1):
            if sieve[num]:  # If num is prime, mark its multiples as non-prime
                for multiple in range(num * num, right + 1, num):
                    sieve[multiple] = False

        # Step 2: Collect primes in range [left, right]
        primes = [num for num in range(left, right + 1) if sieve[num]]

        # Step 3: Find the closest prime pair
        if len(primes) < 2:
            return [-1, -1]

        min_diff = float('inf')
        result = [-1, -1]

        for i in range(len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                result = [primes[i], primes[i + 1]]

        return result
