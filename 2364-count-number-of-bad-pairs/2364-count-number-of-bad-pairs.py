from collections import defaultdict

class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        n = len(nums)
        total_pairs = n * (n - 1) // 2  # Total number of pairs
        count_map = defaultdict(int)
        good_pairs = 0

        for i, num in enumerate(nums):
            val = num - i  # Compute the transformed value
            good_pairs += count_map[val]  # Count previous occurrences (good pairs)
            count_map[val] += 1  # Update count

        return total_pairs - good_pairs  # Bad pairs = Total pairs - Good pairs
