class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        n = len(fruits)
        res = 0
        for i in range(n):
            res += fruits[i][i]
        dp_bottom = [fruits[n-1][0], 0, 0]
        dp_right = [fruits[0][n-1], 0, 0]
        max_reach = 2
        for i in range(1, n - 1):
            new_dp_bottom = [0] * (max_reach + 2)
            new_dp_right = [0] * (max_reach + 2)
            for j in range(max_reach):
                new_dp_bottom[j] = max(dp_bottom[j - 1], dp_bottom[j], dp_bottom[j + 1]) + fruits[n - 1 - j][i]
                new_dp_right[j] = max(dp_right[j -1], dp_right[j], dp_right[j + 1]) + fruits[i][n - 1 - j]
            dp_bottom = new_dp_bottom
            dp_right = new_dp_right
            if max_reach - n + 4 + i <= 1:
                max_reach += 1
            elif max_reach - n + 3 + i > 1:
                max_reach -= 1

        return res + dp_right[0] + dp_bottom[0]