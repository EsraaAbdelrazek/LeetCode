class Solution:
    def totalMoney(self, n: int) -> int:
        t, ans = n, 0
        i = 0
        while i <= n // 7:
            k = i + 1
            if t // 7 == 0:
                for j in range(t):
                    ans += k
                    k += 1
            else:
                for j in range(7):
                    ans += k
                    k += 1
                t -= 7
            i += 1
        return ans