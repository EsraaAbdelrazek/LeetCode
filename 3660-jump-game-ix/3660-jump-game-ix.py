from typing import List

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        suffixMin = [0] * (n + 1)
        suffixMin[n] = float("inf")
        for i in range(n - 1, -1, -1):
            suffixMin[i] = min(nums[i], suffixMin[i + 1])

        ans = [0] * n
        l = 0

        while l < n:
            r = l
            component_max = nums[l]

            while r + 1 < n and component_max > suffixMin[r + 1]:
                r += 1
                component_max = max(component_max, nums[r])

            for i in range(l, r + 1):
                ans[i] = component_max

            l = r + 1

        return ans