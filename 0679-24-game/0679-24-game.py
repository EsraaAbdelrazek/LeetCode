class Solution:
    def judgePoint24(self, cards: list[int]) -> bool:
        def dfs(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6
            n = len(nums)
            for i in range(n):
                for j in range(i+1, n):
                    num1, num2 = nums[i], nums[j]
                    nextNums = [nums[k] for k in range(n) if k != i and k != j]
                    for val in (num1+num2, num1-num2, num2-num1, num1*num2):
                        if dfs(nextNums + [val]):
                            return True
                    if abs(num2) > 1e-6 and dfs(nextNums + [num1/num2]):
                        return True
                    if abs(num1) > 1e-6 and dfs(nextNums + [num2/num1]):
                        return True
            return False
        return dfs(list(map(float, cards)))