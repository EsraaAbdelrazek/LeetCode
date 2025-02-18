class Solution:
    def strStr(self, haystack: str, needle: str) -> int:  # Added 'self' as the first parameter
        # If the needle is an empty string, return 0 as per convention
        if not needle:
            return 0

        return haystack.find(needle)
