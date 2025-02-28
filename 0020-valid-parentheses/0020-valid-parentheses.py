class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to keep track of opening brackets
        stack = []
        # Mapping of closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in bracket_map:  # If it's a closing bracket
                # Pop the top element from the stack if it's not empty, else use a dummy value
                top_element = stack.pop() if stack else '#'
                # If the top element doesn't match the corresponding opening bracket
                if bracket_map[char] != top_element:
                    return False
            else:  # It's an opening bracket
                stack.append(char)
        
        # If the stack is empty, all brackets were matched
        return not stack
