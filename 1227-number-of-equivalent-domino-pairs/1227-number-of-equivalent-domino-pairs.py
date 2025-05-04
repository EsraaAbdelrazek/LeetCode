class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = [0] * 100  # Because max key = 9*10 + 9 = 99
        result = 0

        for a, b in dominoes:
            key = a * 10 + b if a <= b else b * 10 + a
            result += count[key]
            count[key] += 1

        return result