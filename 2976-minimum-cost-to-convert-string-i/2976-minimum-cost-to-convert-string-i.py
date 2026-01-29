class Solution:
    def minimumCost(self, source: str, target: str, original: list[str], changed: list[str], cost: list[int]) -> int:
        arr = [[float('inf')] * 26 for _ in range(26)]
        
        for i in range(26):
            arr[i][i] = 0
        
        for i in range(len(original)):
            val1 = ord(original[i]) - ord('a')
            val2 = ord(changed[i]) - ord('a')
            arr[val1][val2] = min(arr[val1][val2], cost[i])
        
        for i in range(26):
            for j in range(26):
                for k in range(26):
                    arr[j][k] = min(arr[j][k], arr[j][i] + arr[i][k])
        
        ans = 0
        for i in range(len(source)):
            val1 = ord(source[i]) - ord('a')
            val2 = ord(target[i]) - ord('a')

            if val1 == val2:
                continue

            if arr[val1][val2] == float('inf'):
                return -1
            
            ans += arr[val1][val2]
        
        return ans