class Solution:
    def maximum69Number(self, num: int) -> int:
        i = 1000
        while i > 0:
            if (num // i) % 10 == 6:
                num += 3 * i  # flip 6 → 9
                break
            i //= 10
        return num