class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count  = defaultdict (int) 
        for num in nums : 
            if num % 2 ==0 : 
                count [num] +=1 

            
        if not count : 
            return -1 
        mx = max (count.values())
        res = 0 
        frq = []
        for key , value  in count.items() : 
            if value == mx : 
                frq.append (key)
        return min (frq) 
