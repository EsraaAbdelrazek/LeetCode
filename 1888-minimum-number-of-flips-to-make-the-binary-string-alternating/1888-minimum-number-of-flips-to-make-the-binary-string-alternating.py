class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        ss = s + s

        ans = float('inf')
        diff1 = diff2 = 0

        for i in range(len(ss)):

            exp1 = '0' if i % 2 == 0 else '1'
            exp2 = '1' if i % 2 == 0 else '0'

            if ss[i] != exp1:
                diff1 += 1
            if ss[i] != exp2:
                diff2 += 1

            if i >= n:
                p1 = '0' if (i-n) % 2 == 0 else '1'
                p2 = '1' if (i-n) % 2 == 0 else '0'

                if ss[i-n] != p1:
                    diff1 -= 1
                if ss[i-n] != p2:
                    diff2 -= 1

            if i >= n-1:
                ans = min(ans, diff1, diff2)

        return ans