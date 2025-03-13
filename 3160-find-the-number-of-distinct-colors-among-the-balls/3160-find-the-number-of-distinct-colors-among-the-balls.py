from typing import List

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_colors = {}  # Dictionary to store ball color mappings
        color_count = {}  # Dictionary to count occurrences of each color
        result = []
        
        for x, y in queries:
            # If the ball was already colored, decrement count of old color
            if x in ball_colors:
                old_color = ball_colors[x]
                color_count[old_color] -= 1
                if color_count[old_color] == 0:
                    del color_count[old_color]
            
            # Assign new color to the ball
            ball_colors[x] = y
            color_count[y] = color_count.get(y, 0) + 1
            
            # Store the number of distinct colors
            result.append(len(color_count))
        
        return result