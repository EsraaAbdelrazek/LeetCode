class Solution:
    def numSteps(self, s: str) -> int:
        # Convert binary string to a decimal integer
        num = int(s, 2)
        steps = 0

        while num != 1:
            # If even, divide by 2
            if num % 2 == 0:
                num = num // 2
                steps += 1
            else:
            #If odd, add 1 (making it even) then divide by 2
            # This counts as 2 steps
                num += 1
                num = num // 2
                steps += 2

        return steps