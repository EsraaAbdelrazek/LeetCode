class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        print ("ransomNote" ,Counter (ransomNote) )
        print ("magazine" ,Counter (magazine) )
        return Counter (ransomNote) <= Counter (magazine)
        