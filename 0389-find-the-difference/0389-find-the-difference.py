class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
       s = s+t 
       res = 0
       for c in s :  
            res ^= ord (c) 
       return chr (res)
