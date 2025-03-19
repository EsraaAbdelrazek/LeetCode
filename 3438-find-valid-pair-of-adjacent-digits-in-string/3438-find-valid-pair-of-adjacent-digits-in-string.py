from collections import Counter

class Solution:
    def findValidPair(self, s: str) -> str:
        freq = Counter(s)

        for i in range(len(s) - 1):
            a, b = s[i], s[i + 1]
            if a != b:
                if freq[a] == int(a) and freq[b] == int(b):
                    return a + b
        return ""
