from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        res = 0

        for cnt in Counter(s).values():
            if cnt % 2 == 1:
                res += 1
            else:
                res += 2

        return res
