class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = set("aeiou")
        n = len(word)
        res = 0

        for left in range(n):
            consonant = 0
            seen = set()
    
            for right in range(left, n):
                ch = word[right]
                if ch in vowels:
                    seen.add(ch)
                else:
                    consonant += 1
                if consonant > k:
                    break
                if consonant == k and seen == vowels:
                    res += 1
        return res