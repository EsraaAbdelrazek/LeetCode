from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def is_vowel_string(s: str) -> bool:
            vowels = {'a', 'e', 'i', 'o', 'u'}
            return s[0] in vowels and s[-1] in vowels

        n = len(words)
        prefix = [0] * (n + 1)

        
        for i in range(n):
            prefix[i + 1] = prefix[i] + (1 if is_vowel_string(words[i]) else 0)

        
        result = []
        for l, r in queries:
            result.append(prefix[r + 1] - prefix[l])

        return result
