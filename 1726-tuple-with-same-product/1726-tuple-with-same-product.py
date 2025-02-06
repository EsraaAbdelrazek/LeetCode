from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        product_count = defaultdict(int)
        n = len(nums)
        result = 0

        # Step 1: Compute all product pairs and store their counts
        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_count[product] += 1

        # Step 2: Calculate the number of valid tuples
        for count in product_count.values():
            if count > 1:
                result += (count * (count - 1)) // 2  # Choose 2 pairs out of 'count'

        return result * 8  # Each pair contributes 8 valid tuples
