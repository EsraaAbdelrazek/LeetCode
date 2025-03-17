class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        x = Counter (nums) 
        for x, y in x.items () : 
            if y % 2 : 
               
                return False 

        return True 

        