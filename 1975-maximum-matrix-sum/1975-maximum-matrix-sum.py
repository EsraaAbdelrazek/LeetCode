class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:

        res  , nm_neg= 0 , 0 
        mn = float ("inf")
        for row in matrix : 
            for n in row  :
                 res += abs(n) 
                 mn = min (mn , abs(n))

                 if n < 0 : nm_neg += 1  

        if nm_neg & 1 : # if nm_neg is odd 
            res -= (mn * 2)


        


        return res 
        