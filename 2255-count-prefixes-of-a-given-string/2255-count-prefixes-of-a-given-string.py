from typing import List

class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        for word in words:
            if len(word) <= len(s):  # Ensure word is not longer than s
                match = True
                for i in range(len(word)):  # Compare characters manually
                    if word[i] != s[i]:
                        match = False
                        break
                if match:
                    count += 1
        return count
