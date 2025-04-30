class Solution:
    def evenOddBit(self, n: int) -> List[int]:

        bin_num = (bin (n)[2:]) [:: -1]
        even , odd = 0 , 0 

        for i in range (len (bin_num)) : 
            if bin_num [i] == '1' : 
                if i % 2 ==0 : 
                    even +=1 
                else : 
                    odd += 1 
        
        res = [even , odd] 
        return res

        
        