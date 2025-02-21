class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len (nums)
        ans , sol = []  , [] 
        def backtrack () :
           
            if len (sol) == n : 
                ans.append (sol[:]) 
                return 
            
            for i in nums : 
                if i not in sol : 
                    sol .append (i)
                    backtrack ()
                    sol .pop () 
            
        backtrack()
        return ans

        