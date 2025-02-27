class Solution:
    def summaryRanges(self, nums):
        res = []

        if not nums:
            return res

        s = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:  # Correct consecutive check
                continue
            else:
                if s == nums[i - 1]:  # Single number range
                    res.append(str(s))
                else:
                    res.append(str(s) + '->' + str(nums[i - 1]))
                s = nums[i]  # Start a new range

        # Adding the last range after loop ends
        if s == nums[-1]:
            res.append(str(s))
        else:
            res.append(str(s) + '->' + str(nums[-1]))

        return res
