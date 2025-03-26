from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
      
        values = [num for row in grid for num in row]
        
       
        remainder = values[0] % x
        if any(num % x != remainder for num in values):
            return -1 
        
      
        values.sort()
        median = values[len(values) // 2]  
        
  
        operations = sum(abs(num - median) // x for num in values)
        
        return operations
