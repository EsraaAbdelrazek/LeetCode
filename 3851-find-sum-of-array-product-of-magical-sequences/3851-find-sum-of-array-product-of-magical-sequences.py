# Python3 Solution
MOD = 10**9 + 7
C = [[0] * 31 for _ in range(31)]

for i in range(1, 31):
    C[i][0] = C[i][i] = 1
    for j in range(1, i // 2 + 1):
        C[i][j] = C[i][i - j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD

from functools import lru_cache

class Solution:
    def magicalSum(self, m: int, k: int, nums: list[int]) -> int:
        n = len(nums)

        @lru_cache(None)
        def dfs(m, k, i, flag):
            bz = bin(flag).count("1")
            if m < 0 or k < 0 or m + bz < k:
                return 0
            if m == 0:
                return 1 if k == bz else 0
            if i >= n:
                return 0

            ans, powX = 0, 1
            x = nums[i]
            for f in range(m + 1):
                perm = (C[m][f] * powX) % MOD
                newFlag = flag + f
                nextFlag = newFlag >> 1
                bitSet = newFlag & 1
                ans = (ans + perm * dfs(m - f, k - bitSet, i + 1, nextFlag)) % MOD
                powX = (powX * x) % MOD
            return ans

        return dfs(m, k, 0, 0)