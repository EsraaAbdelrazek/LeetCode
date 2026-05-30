class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = 0
        upper = 0

        for ch in word:
            if ch.islower():
                lower |= (1 << (ord(ch) - ord('a')))
            else:
                upper |= (1 << (ord(ch) - ord('A')))

        common = lower & upper

        # counting number of set bits
        return common.bit_count()