from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        maxCount, res = 0, 0
        
        for num in nums:
            count[num] = count.get(num, 0) + 1 
            if count[num] > maxCount:
                maxCount = count[num]
                res = num
        
        return res  
