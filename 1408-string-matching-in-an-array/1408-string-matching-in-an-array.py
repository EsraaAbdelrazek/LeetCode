
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = set()  # Using a set to avoid duplicates
        for word in words:
            for other_word in words:
                if word != other_word and word in other_word:  # Ensure it's a substring of a different word
                    result.add(word)
        return list(result)  # Convert set to list before returning