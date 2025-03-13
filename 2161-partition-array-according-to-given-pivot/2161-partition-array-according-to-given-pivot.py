class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        less, equal, greater = [], [], []
        
       
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)
        
      
        return less + equal + greater
