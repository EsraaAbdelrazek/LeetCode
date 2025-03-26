from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Flatten the grid into a list
        values = [num for row in grid for num in row]
        
        # Check if all elements have the same remainder when divided by x
        remainder = values[0] % x
        if any(num % x != remainder for num in values):
            return -1  # Not possible
        
        # Sort the values to find the median
        values.sort()
        median = values[len(values) // 2]  # Median minimizes operations
        
        # Compute the total operations needed
        operations = sum(abs(num - median) // x for num in values)
        
        return operations
