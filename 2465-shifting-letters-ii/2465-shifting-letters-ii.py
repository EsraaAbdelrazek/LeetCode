class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefixSum = [0] * (n + 1)
        
        for start, end, direction in shifts:
            value = 1 if direction == 1 else -1
            prefixSum[start] += value
            prefixSum[end + 1] -= value
        
        for i in range(1, n):
            prefixSum[i] += prefixSum[i-1]
            
        result = list(s)
        for i in range(n):
            totalShifts = prefixSum[i]
            totalShifts = ((totalShifts % 26) + 26) % 26
            
            newChar = (ord(s[i]) - ord('a') + totalShifts) % 26
            result[i] = chr(ord('a') + newChar)
        
        return ''.join(result)