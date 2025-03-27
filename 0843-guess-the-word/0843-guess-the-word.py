from typing import List
from collections import Counter

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        def match(w1, w2):
            """Calculate the number of matching characters in the same position"""
            return sum(c1 == c2 for c1, c2 in zip(w1, w2))

        while words:
        
            count_candidates = []
            
            for word in words:
                count = [0] * 7 
                for w in words:
                    if word != w:
                        matches = match(word, w)
                        count[matches] += 1
                
            
                count_candidates.append((max(count), word))

            _, best_word = min(count_candidates)
            
         
            matches = master.guess(best_word)
          
            if matches == 6:
                return  
            
           
            words = [w for w in words if match(w, best_word) == matches]
