class Solution:
    def clearDigits(self, s: str) -> str:
       
        stack = []
        
        for char in s:
            if char.isdigit():
                # Remove the closest non-digit character from the left
                for i in range(len(stack) - 1, -1, -1):
                    if not stack[i].isdigit():
                        stack.pop(i)
                        break
            else:
                stack.append(char)

        return "".join(stack)
            