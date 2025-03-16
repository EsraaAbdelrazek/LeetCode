class Solution(object):
    def isPalindrome(self, x):
       
    
    #     if x < 0 or (x % 10 == 0 and x != 0):
    #         return False
    
    #     reversed_half = 0
    #     while x > reversed_half:
    #     # Extract the last digit and add it to the reversed half
    #         reversed_half = reversed_half * 10 + x % 10
    #     # Remove the last digit from x
    #         x //= 10
    
    # # Check if the original number is equal to the reversed half
    # # For odd-length numbers, we can ignore the middle digit by reversed_half // 10
    #     return x == reversed_half or x == reversed_half // 10

        xstr = str (x) 
        return xstr[::] ==xstr [::-1]