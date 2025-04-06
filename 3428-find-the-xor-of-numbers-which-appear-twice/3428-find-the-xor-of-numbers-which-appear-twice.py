class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        res = 0 
        duplt = Counter (nums)
        for i , j in duplt.items () : 
            if j == 2 : 
                res ^= i 
        return res 



        