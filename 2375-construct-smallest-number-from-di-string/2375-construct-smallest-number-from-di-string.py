class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack = []
        result = ""
        num = 1 
        
        for ch in pattern:
            stack.append(str(num))
            num += 1
            
            if ch == 'I':
                while stack:
                    result += stack.pop()
        
        stack.append(str(num)) 
        while stack:
            result += stack.pop()
        
        return result
            