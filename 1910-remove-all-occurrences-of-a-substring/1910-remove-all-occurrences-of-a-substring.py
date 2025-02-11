class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        part_len = len(part)

        for char in s:
            stack.append(char)  # Append character
            if len(stack) >= part_len and ''.join(stack[-part_len:]) == part:
                del stack[-part_len:]  # Remove last `part_len` characters

        return ''.join(stack)
