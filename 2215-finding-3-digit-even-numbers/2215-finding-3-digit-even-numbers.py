from itertools import permutations
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = set () 

        for a , b , c in permutations (digits , 3) : 
            if a == 0 : 
                continue 
            number = a * 100 + b * 10 + c 
            if number % 2 ==0 : 
                res.add (number) 

        return sorted (res) 
        