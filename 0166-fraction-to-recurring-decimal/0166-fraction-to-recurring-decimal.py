class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        fraction = []
        if (numerator < 0) ^ (denominator < 0):
            fraction.append("-")

        dividend = abs(numerator)
        divisor = abs(denominator)
        fraction.append(str(dividend // divisor))
        remainder = dividend % divisor
        if remainder == 0:
            return "".join(fraction)

        fraction.append(".")
        map_dict = {}
        while remainder != 0:
            if remainder in map_dict:
                fraction.insert(map_dict[remainder], "(")
                fraction.append(")")
                break
            map_dict[remainder] = len(fraction)
            remainder *= 10
            fraction.append(str(remainder // divisor))
            remainder %= divisor

        return "".join(fraction)


    # def fractionToDecimal(n: int, d: int) -> str:
    #     if n == 0: return "0"  # numerator is zero, done
    #     res = "-" if (n < 0) ^ (d < 0) else ""
    #     n, d = abs(n), abs(d)
    #     res += str(n // d)
    #     n %= d
    #     if not n: return res  # divides cleanly
    #     res += "."
    #     seen = {}
    #     while n:
    #         if n in seen:  # cycle spotted
    #             return res[:seen[n]] + "(" + res[seen[n]:] + ")"
    #         seen[n] = len(res)
    #         n *= 10
    #         res += str(n // d)
    #         n %= d
    #     return res