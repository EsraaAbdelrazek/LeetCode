class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len (grid)
        org = [n for n in range (1 , n**2 +1 )  ]
        flatten =[i  for subgrid in grid for i in subgrid  ] 
        hashmap = Counter (flatten)
        repeated = [key for key , value in hashmap. items () if value > 1] 
        missing = [n for n in org if n not in flatten  ] 

        res = repeated + missing
        return res  

        