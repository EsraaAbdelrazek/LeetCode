from typing import List

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        sormadexin = nums
        max_val = max(sormadexin)
        min_val = min(sormadexin)
        return k * (max_val - min_val)
