class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        cur , res , min_pre , max_pre = 0 , 0 , 0 , 0  

        for num in nums : 
            cur += num 
            res = max (res , abs (cur - min_pre) , abs (cur - max_pre))
            min_pre = min (min_pre , cur ) 
            max_pre = max (max_pre , cur ) 
        return res 
        