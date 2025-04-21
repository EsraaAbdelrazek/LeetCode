from typing import List

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_prefix = 0
        max_prefix = 0
        prefix = 0

        for diff in differences:
            prefix += diff
            min_prefix = min(min_prefix, prefix)
            max_prefix = max(max_prefix, prefix)

        # Compute the valid range for the first element of the sequence
        min_x = lower - min_prefix
        max_x = upper - max_prefix

        return max(0, max_x - min_x + 1)
