class Solution {
public:
    bool isPalindrome(int x) {
        // Negative numbers and numbers ending with 0 (except 0 itself) cannot be       palindromes
        if (x < 0 || (x % 10 == 0 && x != 0)) {
            return false;
        }
        
        int reversedHalf = 0;
        while (x > reversedHalf) {
            // Extract the last digit and add it to the reversed half
            reversedHalf = reversedHalf * 10 + x % 10;
            // Remove the last digit from x
            x /= 10;
        }
        
        // Check if the original number is equal to the reversed half
        // For odd-length numbers, ignore the middle digit by reversedHalf / 10
        return x == reversedHalf || x == reversedHalf / 10;
    }
};
