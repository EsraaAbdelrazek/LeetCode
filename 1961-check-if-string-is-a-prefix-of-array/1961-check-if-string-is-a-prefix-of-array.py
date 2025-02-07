from typing import List

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        prefix = ""
        for word in words:
            prefix += word  # Concatenate words one by one
            if prefix == s:  # If prefix matches s, return True
                return True
            if len(prefix) > len(s):  # If prefix exceeds s, return False
                return False
        return False  # If no match is found, return False
