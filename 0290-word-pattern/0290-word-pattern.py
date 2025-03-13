class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()  # Split the sentence into words

        if len(pattern) != len(words):
            return False  # If lengths don't match, pattern is invalid

        char_to_word = {}
        word_to_char = {}

        for char, word in zip(pattern, words):
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False  # Mismatch in existing mapping
            else:
                char_to_word[char] = word
            
            if word in word_to_char:
                if word_to_char[word] != char:
                    return False  # Mismatch in existing mapping
            else:
                word_to_char[word] = char

        return True
