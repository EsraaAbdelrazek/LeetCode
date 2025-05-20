class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        line = [0 for i in range(len(nums) + 1)]

        for start, end in queries:
            line[start] += 1
            line[end + 1] -= 1

        for i in range(1, len(line)):
            line[i] += line[i - 1]

        for i in range(len(nums)):
            if line[i] < nums[i]:
                return False

        return True
