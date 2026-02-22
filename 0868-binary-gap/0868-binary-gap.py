class Solution:
    def binaryGap(self, n: int) -> int:
        binary = format(n, "b")
        prev = -1
        res = 0
        for i in range(len(binary)):
            if binary[i] == "1":
                if prev != -1:
                    res = max(res, i - prev)
                prev = i
        return res