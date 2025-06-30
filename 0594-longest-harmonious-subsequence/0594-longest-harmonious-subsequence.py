class Solution:
    def findLHS(self, nums):
        from collections import Counter
        freq = Counter(nums)
        ans = 0
        for key in freq:
            if key + 1 in freq:
                ans = max(ans, freq[key] + freq[key + 1])
        return ans