class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = 0 
        for i in range (len (nums) -1) : 
            for j in range (i , len (nums) ) : 
                if nums [i] == nums [j] and i < j : 
                    c +=1 

        return c 