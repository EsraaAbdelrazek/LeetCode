class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) != 2:
            s1 = ""
            for i in range(1, len(s)):
                x = ((ord(s[i]) - ord('a')) + (ord(s[i - 1]) - ord('a'))) % 10
                s1 += chr(x + ord('a'))
            s = s1
        return s[0] == s[1]