class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        resstr = ""
        for i in digits : 
            resstr += str (i) 
        
        resint = int (resstr) 
        resint += 1 

        return [ int (i) for i in str (resint)]