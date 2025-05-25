class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        res = 0
        diff = defaultdict(int)
        same = defaultdict(int)

        for w in words:
            if w[0] == w[1]:
                res += 2
                same[w[0]] += 1
            elif diff[w[::-1]] != 0:
                res += 4
                diff[w[::-1]] -= 1
            else:
                diff[w] += 1

        odds = 0
        for c in same:
            if same[c] % 2:
                odds += 1
                if odds > 1:
                    res -= 2

        return res
