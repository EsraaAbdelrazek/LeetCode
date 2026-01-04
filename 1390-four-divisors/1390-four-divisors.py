class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        sm = 0
        
        for i in nums:
            cursm = 0
            numdiv = 0
            
            for div in range(1, int(i ** 0.5) + 1):
                if i % div == 0:
                    numdiv += 1
                    cursm += div
                    
                    other = i // div
                    if other != div:
                        numdiv += 1
                        cursm += other
            
            if numdiv == 4:
                sm += cursm
        
        return sm
