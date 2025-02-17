from itertools import permutations

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        unique_sequences = set()
        
     
        for i in range(1, len(tiles) + 1):
            for p in permutations(tiles, i):
                unique_sequences.add(p)  
        
        return len(unique_sequences)



