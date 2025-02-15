class Solution:
    def punishmentNumber(self, n: int) -> int:
        def canPar (index ,cur_sum , target ,   s ) : 
            if index == len (s) : 
                return cur_sum == target 

            for j in range (index , len (s) ) : 
                num = int (s[index : j+1])
                
                if cur_sum + num > target : 
                    return False 

                if canPar (j+1 , cur_sum + num , target , s) : 
                    return True 
            return False 

        total = 0 
        for i in range (1 , n+1) :
            sqr = str (i * i) 
            if canPar (0 , 0 , i , sqr) :  
              total += i*i

        return total 
                