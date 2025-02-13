class Solution:
    def romanToInt(self, s: str) -> int:
        # Define a mapping of Roman numerals to integers
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Traverse the Roman numeral string from left to right
        for char in s:
            # Get the integer value of the current Roman numeral
            curr_value = roman_to_int[char]
            
            # If the current value is greater than the previous one,
            # subtract twice the previous value (to adjust for previous addition)
            if curr_value > prev_value:
                total += curr_value - 2 * prev_value
            else:
                total += curr_value
            
            # Update the previous value for the next iteration
            prev_value = curr_value
        
        return total