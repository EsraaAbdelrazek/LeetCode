class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if not s:
            return 0
        n = len(s)
        curr = 1
        prev, res = 0, 0
        for i in range(1, n):
            if s[i] == s[i - 1]:
                curr += 1
            else:
                prev = curr
                curr = 1
            if curr <= prev:
                res += 1
        return res