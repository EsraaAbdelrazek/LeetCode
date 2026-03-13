class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        s = sum(workerTimes)
        n = len(workerTimes)
        v = ceil(mountainHeight / n)
        start, end = 1, v * (v + 1) * max(workerTimes) // 2
        while start < end:
            mid = (start + end) // 2
            w = 0
            for t in workerTimes:
                w += floor(sqrt(2 * mid / t + 0.25) - 0.5)
            if w >= mountainHeight:
                end = mid
            else:
                start = mid + 1
        return start