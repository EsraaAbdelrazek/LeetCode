from typing import List
from collections import Counter

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        def match(w1, w2):
            """Calculate the number of matching characters in the same position"""
            return sum(c1 == c2 for c1, c2 in zip(w1, w2))

        while words:
            # Step 1: Choose the best word based on minimax strategy
            count_candidates = []
            
            for word in words:
                count = [0] * 7  # Since words are 6-letter long, we track match counts from 0 to 6
                for w in words:
                    if word != w:
                        matches = match(word, w)
                        count[matches] += 1
                
                # Store (max frequency of a match count, word) to minimize worst-case scenario
                count_candidates.append((max(count), word))

            # Step 2: Pick the word that minimizes the worst-case scenario
            _, best_word = min(count_candidates)
            
            # Step 3: Guess the chosen word
            matches = master.guess(best_word)
            
            # Step 4: If the word is correct (all 6 characters match), return
            if matches == 6:
                return  
            
            # Step 5: Filter words that have the same number of matches with the guessed word
            words = [w for w in words if match(w, best_word) == matches]
