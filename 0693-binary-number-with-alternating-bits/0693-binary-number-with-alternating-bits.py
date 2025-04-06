class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        c1 = bin (n).count ('11')
        c2 = bin (n).count ('00')
        if c1 or c2 : 
            return False 
        else : 
            return True 