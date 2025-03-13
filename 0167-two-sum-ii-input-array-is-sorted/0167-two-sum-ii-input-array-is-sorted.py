from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1

        while i <= j:
            sum_ = numbers[i] + numbers[j]
            if sum_ > target:
                j -= 1
            elif sum_ < target:
                i += 1
            else:
                break
        
        return [i + 1, j + 1]
