from typing import List

class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        stack = []
        for num in nums:
          
            while stack and stack[-1] > num:
                top = stack.pop()
                num = max(num, top)
            stack.append(num)
        return len(stack)
