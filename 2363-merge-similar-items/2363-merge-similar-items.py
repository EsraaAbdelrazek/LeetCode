class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        total = Counter ()

        for i , j in items1 : 
            total [i] += j

        for i , j in items2 : 
            total [i] += j

        return list (sorted (total.items()))


        