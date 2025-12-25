class Solution:
    def maximumHappinessSum(self, h: List[int], k: int) -> int:
        h.sort(reverse=True)
        i=0 
        Ans=0
        while k>0 and h[i]-i>0:
            Ans+=h[i]-i
            i+=1
            k-=1
        return Ans
            
        
        