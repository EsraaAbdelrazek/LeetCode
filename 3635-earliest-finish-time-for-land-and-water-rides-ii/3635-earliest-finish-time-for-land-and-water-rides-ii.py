class Solution:
    def calFinishTime(self, ls, ld, ws, wd):
        mini = float('inf')
        ans = float('inf')

        for i in range(len(ls)):
            mini = min(mini, ls[i] + ld[i])

        for i in range(len(ws)):
            finish = max(mini, ws[i]) + wd[i]
            ans = min(ans, finish)

        return ans

    def earliestFinishTime(self, landStartTime, landDuration,
                           waterStartTime, waterDuration):

        landFirst = self.calFinishTime(
            landStartTime, landDuration,
            waterStartTime, waterDuration
        )

        waterFirst = self.calFinishTime(
            waterStartTime, waterDuration,
            landStartTime, landDuration
        )

        return min(landFirst, waterFirst)