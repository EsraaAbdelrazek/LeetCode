class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        result = "1"
        
        for _ in range(2, n + 1):
            current = ""
            count = 1
            
            for j in range(1, len(result)):
                if result[j] == result[j - 1]:
                    count += 1
                else:
                    current += str(count) + result[j - 1]
                    count = 1
            
            current += str(count) + result[-1]  # Add the last group
            result = current
        
        return result
