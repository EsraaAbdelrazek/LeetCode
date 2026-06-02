class Solution:
    def earliestFinishTime(self, landStartTime, landDuration,
                           waterStartTime, waterDuration):

        land_finish = min(
            landStartTime[i] + landDuration[i]
            for i in range(len(landStartTime))
        )

        opt1 = min(
            max(land_finish, waterStartTime[i]) + waterDuration[i]
            for i in range(len(waterStartTime))
        )

        water_finish = min(
            waterStartTime[i] + waterDuration[i]
            for i in range(len(waterStartTime))
        )

        opt2 = min(
            max(water_finish, landStartTime[i]) + landDuration[i]
            for i in range(len(landStartTime))
        )

        return min(opt1, opt2)