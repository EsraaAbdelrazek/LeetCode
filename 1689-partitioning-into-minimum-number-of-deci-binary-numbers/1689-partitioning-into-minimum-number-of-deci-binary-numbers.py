class Solution:
    def minPartitions(self, n: str) -> int:
        # The largest digit in n determines the answer
        # Check from 9 → 1 and return the first digit found
        for d in "987654321":
            if d in n:
                return int(d)