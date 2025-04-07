class Solution:
    # def splitNum(self, num: int) -> int:
        
    #     digits = sorted(str(num))
    #     num1 = ""
    #     num2 = ""
        
    #     for i, digit in enumerate(digits):
    #         if len(num1) <= len(num2):
    #             num1 += digit
    #         else:
    #             num2 += digit

    #     return int(num1) + int(num2)
        def splitNum(self, num: int) -> int:
            s = ''.join(sorted(str(num)))
            return int(s[::2]) + int(s[1::2])
