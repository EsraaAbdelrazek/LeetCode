# class Solution:
#     def distributeCandies(self, n: int, limit: int) -> int:
#         ans = 0
#         for i in range(min(limit, n) + 1):
#             if n - i > 2 * limit:
#                 continue
#             ans += min(n - i, limit) - max(0, n - i - limit) + 1
#         return ans

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if n <= limit:
            return (n+2) * (n+1) // 2
        
        n2 = n - 2 * limit
        n3 = (n + n2) // 2

        result = 0

        if n2 < 0:
            result += (n3 + 1) * (1 - n2)
            result += (limit+1 - (n3+1)) * (n + 1)
            result += (n3+1) * (n3) // 2
            if n3+1 <= limit+1:
                result -= (n3+1 + limit) * (limit+1 - n3-1) // 2
        else:
            d = min(limit+1, n3+1)
            result += max(0, d - n2) * (1 - n2)
            result += max(0, limit+1 - d) * (1 + n)
            if n2 <= limit+1:
                result += (n2 + limit) * (limit+1 - n2) // 2
        
        return result

            