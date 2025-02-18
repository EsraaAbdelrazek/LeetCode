class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        per = [] 
        n = len (s)
        l , r = 0 , n 

        for i in s : 
            if  i == 'I' : 
                per.append(l) 
                l+=1 
            else  :
                per.append (r) 
                r -=1 
        per .append (l) 
        return per  

        