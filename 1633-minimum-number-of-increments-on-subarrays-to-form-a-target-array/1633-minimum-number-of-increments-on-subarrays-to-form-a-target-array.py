class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        result = prev = 0
        for x in target:
            if x > prev:
                result += x - prev
            prev = x
        return result