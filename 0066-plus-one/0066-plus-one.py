class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s =''
        for i in digits : 
            s+= str (i)

        n = int (s) 
        n+=1 
        s = str (n) 
        res = [] 
        for i in s : 
            res.append (int (i) ) 
        return res
        