from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total_sum = sum(sum(row) for row in grid)

        if total_sum % 2 != 0:
            return False 

        target = total_sum // 2

     
        curr_sum = 0
        for i in range(m - 1):  
            curr_sum += sum(grid[i])
            if curr_sum == target:
                return True

       
        col_sums = [0] * n
        for r in range(m):
            for c in range(n):
                col_sums[c] += grid[r][c]

        curr_sum = 0
        for j in range(n - 1):  
            curr_sum += col_sums[j]
            if curr_sum == target:
                return True

        return False
