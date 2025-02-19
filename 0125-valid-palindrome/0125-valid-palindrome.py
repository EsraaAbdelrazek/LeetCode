class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        newstr = "" 
        for c in s : 
            if c.isalnum() : 
                newstr += c.lower ()

        return newstr == newstr [::-1] 
        

        